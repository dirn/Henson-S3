"""Test Henson-S3."""

import pytest


@pytest.mark.asyncio
async def test_check(s3, check_session):
    """Test check."""
    assert await s3.check('key')


@pytest.mark.asyncio
async def test_check_forbidden(s3, forbidden_session):
    """Test check handles forbidden files."""
    assert not await s3.check('key')


@pytest.mark.asyncio
async def test_check_not_found(s3, not_found_session):
    """Test check handles files that don't exist."""
    assert not await s3.check('key')


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
