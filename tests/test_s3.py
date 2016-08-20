"""Test Henson-S3."""

import pytest


@pytest.mark.asyncio
async def test_download(s3, download_session):
    """Test download."""
    actual = await s3.download('key')
    assert actual


@pytest.mark.asyncio
async def test_upload(s3, upload_session):
    """Test upload."""
    await s3.upload('key', 'value')
    assert True
