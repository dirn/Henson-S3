"""Test utilities."""

from functools import partial
import os

from henson import Application
import placebo
import pytest

from henson_s3 import S3


placebo_fixture = partial(
    os.path.join, os.path.dirname(__file__), 'data', 'placebo')


class MockConsumer:
    """A stubbed consumer class."""

    async def read(self):
        """A stubbed read."""
        return 1


@pytest.fixture
def s3(test_app):
    """Return an instance of the S3 plugin."""
    s3 = S3()
    s3.init_app(test_app)

    return s3


@pytest.fixture
def test_app(test_consumer, event_loop):
    """Return a test application."""
    async def callback(app, message):
        raise Exception('testing')

    app = Application('testing', callback=callback, consumer=test_consumer)
    app.settings['AWS_ACCESS_KEY_ID'] = 'testing'
    app.settings['AWS_SECRET_ACCESS_KEY'] = 'testing'
    app.settings['AWS_BUCKET_NAME'] = 'testing'
    app.settings['AWS_REGION_NAME'] = 'us-east-1'

    @app.message_acknowledgement
    async def stop_loop(app, message):
        event_loop.stop()

    return app


@pytest.fixture
def test_consumer():
    """Return a mock consumer."""
    return MockConsumer()


@pytest.fixture
def check_session(s3, test_app, event_loop):
    """Return a session with placebo attached to it."""
    pill = placebo.attach(s3._session, data_path=placebo_fixture('check'))

    event_loop.run_until_complete(s3._connect(test_app))

    pill.playback()

    return pill


@pytest.fixture
def download_session(s3, test_app, event_loop):
    """Return a session with placebo attached to it."""
    pill = placebo.attach(s3._session, data_path=placebo_fixture('download'))

    event_loop.run_until_complete(s3._connect(test_app))

    pill.playback()

    return pill


@pytest.fixture
def forbidden_session(s3, test_app, event_loop):
    """Return a session with placebo attached to it."""
    pill = placebo.attach(s3._session, data_path=placebo_fixture('forbidden'))

    event_loop.run_until_complete(s3._connect(test_app))

    pill.playback()

    return pill


@pytest.fixture
def not_found_session(s3, test_app, event_loop):
    """Return a session with placebo attached to it."""
    pill = placebo.attach(s3._session, data_path=placebo_fixture('not_found'))

    event_loop.run_until_complete(s3._connect(test_app))

    pill.playback()

    return pill


@pytest.fixture
def upload_session(s3, test_app, event_loop):
    """Return a session with placebo attached to it."""
    pill = placebo.attach(s3._session, data_path=placebo_fixture('upload'))

    event_loop.run_until_complete(s3._connect(test_app))

    pill.playback()

    return pill
