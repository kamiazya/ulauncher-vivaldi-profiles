import subprocess
import json
from typing import Iterable, Optional, NamedTuple
from pathlib import Path

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.BaseAction import BaseAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction


class Profile(NamedTuple):
    dir: str
    name: str
    user_name: str


class VivaldiProfileScanner:
    config_dir: Path

    def __init__(self, config_dir: str) -> None:
        self.config_dir = Path(config_dir).expanduser()

    @property
    def __local_state(self):
        with open(self.config_dir / 'Local State', 'r') as f:
            return json.load(f)

    @property
    def _profile_info_cache(self) -> Iterable[Profile]:
        for dir_, profile_data in self.__local_state['profile']['info_cache'].items():
            yield Profile(
                dir=dir_,
                name=profile_data['name'],
                user_name= profile_data['user_name'],
            )


    def scan(self, query: Optional[str]) -> Iterable[Profile]:
        for profile in self._profile_info_cache:
            if (self.config_dir / profile.dir).exists():
                if query is None or query in profile.name:
                    yield profile


class KeywordQueryEventListener(EventListener):
    def on_event(self, event: KeywordQueryEvent, extension: Extension) -> BaseAction:
        vivaldi_dir = extension.preferences['vivaldi_dir']
        scanner = VivaldiProfileScanner(vivaldi_dir)
        query: Optional[str] = event.get_argument()

        # Create launcher entries
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name=profile.name,
                description=profile.user_name,
                on_enter=ExtensionCustomAction({
                    'profile': profile.dir,
                }, keep_app_open=True)
            )
            for profile in scanner.scan(query)
        ])


class ItemEnterEventListener(EventListener):
    def on_event(self, event: ItemEnterEvent, extension: Extension):
        # Open Chrome when user selects an entry
        data = event.get_data()
        subprocess.Popen([
            extension.preferences['vivaldi_path'],
            f'--profile-directory={data["profile"]}',
        ])


class VivaldiProfileExtension(Extension):
    def __init__(self):
        super(VivaldiProfileExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


if __name__ == '__main__':
    VivaldiProfileExtension().run()
