from datetime import datetime, timedelta, timezone

import pytest
from model_bakery import baker

from ...models import Show, ShowInstance


def test_show_live_enabled():
    show = Show(
        name="My Test Show",
        description="My test show description",
    )
    assert not show.live_enabled

    show.live_auth_registered = True
    assert show.live_enabled

    show.live_auth_custom = True
    assert show.live_enabled


@pytest.mark.django_db
def test_show_instance_get_current():
    now = datetime.now(tz=timezone.utc)
    show_instance: ShowInstance = baker.make(
        "schedule.ShowInstance",
        starts_at=now - timedelta(minutes=5),
        ends_at=now + timedelta(minutes=5),
        modified=False,
    )

    current: ShowInstance = ShowInstance.get_current(when=now)
    assert current.id == show_instance.id
    assert current.starts_at.replace(tzinfo=timezone.utc) == show_instance.starts_at
    assert current.ends_at.replace(tzinfo=timezone.utc) == show_instance.ends_at
