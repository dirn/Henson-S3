"""Test Doozer-S3."""

import pytest


@pytest.mark.asyncio
async def test_check(s3, check_session):
    """Test check."""
    assert await s3.check('key')


@pytest.mark.asyncio
async def test_check_errors(s3, error_session):
    """Test check handles errors."""
    assert not await s3.check('key')


@pytest.mark.asyncio
async def test_download(s3, download_session):
    """Test download."""
    actual = await s3.download('key')
    assert actual


@pytest.mark.asyncio
async def test_download_filenotfounderror(s3, error_session):
    """Test that download raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        await s3.download('key')


@pytest.mark.asyncio
async def test_upload(s3, upload_session):
    """Test upload."""
    await s3.upload('key', 'value')
    assert True
