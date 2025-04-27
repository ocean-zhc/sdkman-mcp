"""SDKMAN! MCP Server module."""

import logging
import os
from typing import Optional, Dict, Any

from mcp.server.fastmcp import FastMCP, Context

from .sdk_commands import (
    sdk_list, sdk_list_candidate, 
    sdk_current, sdk_current_candidate,
    sdk_install, sdk_uninstall,
    sdk_use, sdk_default, sdk_home,
    sdk_env, sdk_upgrade, 
    sdk_version, sdk_offline,
    sdk_selfupdate, sdk_update,
    sdk_flush, sdk_help, sdk_config
)

logger = logging.getLogger(__name__)


def create_server() -> FastMCP:
    """Create and configure the SDKMAN MCP server."""
    server = FastMCP("SDKMAN", 
                     description="SDKMAN! SDK Manager for managing parallel versions of multiple SDKs")
    
    # Register all tools
    
    @server.tool()
    def sdk_list_all() -> Dict[str, Any]:
        """List all available SDK candidates in SDKMAN."""
        logger.info("Listing all SDK candidates")
        return sdk_list()
    
    @server.tool()
    def sdk_list_versions(candidate: str) -> Dict[str, Any]:
        """List all available versions for a specific SDK candidate.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
        """
        logger.info(f"Listing versions for {candidate}")
        return sdk_list_candidate(candidate)
    
    @server.tool()
    def sdk_current_all() -> Dict[str, Any]:
        """Show current versions of all installed SDKs."""
        logger.info("Getting current versions for all SDKs")
        return sdk_current()
    
    @server.tool()
    def sdk_current_version(candidate: str) -> Dict[str, Any]:
        """Show the current version of a specific SDK candidate.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
        """
        logger.info(f"Getting current version for {candidate}")
        return sdk_current_candidate(candidate)
    
    @server.tool()
    def sdk_install_version(candidate: str, version: Optional[str] = None, path: Optional[str] = None) -> Dict[str, Any]:
        """Install a specific version of an SDK candidate.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
            version: Version to install (Optional, installs latest stable if not specified)
            path: Path to local installation (Optional, for local installations)
        """
        logger.info(f"Installing {candidate} {version or 'latest'} {path or ''}")
        return sdk_install(candidate, version, path)
    
    @server.tool()
    def sdk_uninstall_version(candidate: str, version: str) -> Dict[str, Any]:
        """Uninstall a specific version of an SDK candidate.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
            version: Version to uninstall
        """
        logger.info(f"Uninstalling {candidate} {version}")
        return sdk_uninstall(candidate, version)
    
    @server.tool()
    def sdk_use_version(candidate: str, version: str) -> Dict[str, Any]:
        """Use a specific version of an SDK candidate in the current shell.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
            version: Version to use
        """
        logger.info(f"Using {candidate} {version}")
        return sdk_use(candidate, version)
    
    @server.tool()
    def sdk_set_default(candidate: str, version: str) -> Dict[str, Any]:
        """Set the default version of an SDK candidate.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
            version: Version to set as default
        """
        logger.info(f"Setting default {candidate} to {version}")
        return sdk_default(candidate, version)
    
    @server.tool()
    def sdk_get_home(candidate: str, version: str) -> Dict[str, Any]:
        """Get the home directory of a specific version of an SDK candidate.
        
        Args:
            candidate: Name of the SDK candidate (e.g., java, gradle, kotlin)
            version: Version to get home directory for
        """
        logger.info(f"Getting home directory for {candidate} {version}")
        return sdk_home(candidate, version)
    
    @server.tool()
    def sdk_manage_env(action: Optional[str] = None) -> Dict[str, Any]:
        """Manage the .sdkmanrc file for the current directory.
        
        Args:
            action: Action to perform, can be 'init', 'install', or 'clear'
        """
        logger.info(f"Managing .sdkmanrc with action: {action or 'none'}")
        return sdk_env(action)
    
    @server.tool()
    def sdk_check_upgrade(candidate: Optional[str] = None) -> Dict[str, Any]:
        """Check for available upgrades or upgrade a specific candidate.
        
        Args:
            candidate: Name of the SDK candidate to upgrade (Optional, checks all if not specified)
        """
        logger.info(f"Checking upgrades for {candidate or 'all candidates'}")
        return sdk_upgrade(candidate)
    
    @server.tool()
    def sdk_get_version() -> Dict[str, Any]:
        """Display the SDKMAN version."""
        logger.info("Getting SDKMAN version")
        return sdk_version()
    
    @server.tool()
    def sdk_set_offline(mode: str) -> Dict[str, Any]:
        """Enable or disable offline mode.
        
        Args:
            mode: Must be 'enable' or 'disable'
        """
        logger.info(f"Setting offline mode to {mode}")
        return sdk_offline(mode)
    
    @server.tool()
    def sdk_self_update(force: bool = False) -> Dict[str, Any]:
        """Update SDKMAN itself.
        
        Args:
            force: Force update even if there is no new version available
        """
        logger.info(f"Updating SDKMAN {'with force' if force else ''}")
        return sdk_selfupdate(force)
    
    @server.tool()
    def sdk_update_candidates() -> Dict[str, Any]:
        """Update SDKMAN candidates."""
        logger.info("Updating SDKMAN candidates")
        return sdk_update()
    
    @server.tool()
    def sdk_flush_state(mode: Optional[str] = None) -> Dict[str, Any]:
        """Flush SDKMAN local state.
        
        Args:
            mode: What to flush, can be 'tmp', 'metadata', or 'version'. Flushes all if not specified.
        """
        logger.info(f"Flushing SDKMAN state: {mode or 'all'}")
        return sdk_flush(mode)
    
    @server.tool()
    def sdk_get_help(command: Optional[str] = None) -> Dict[str, Any]:
        """Get help about SDKMAN or a specific command.
        
        Args:
            command: Command to get help for (Optional, shows general help if not specified)
        """
        logger.info(f"Getting help for {command or 'SDKMAN'}")
        return sdk_help(command)
    
    @server.tool()
    def sdk_edit_config() -> Dict[str, Any]:
        """Edit the SDKMAN configuration."""
        logger.info("Editing SDKMAN configuration")
        return sdk_config()
    
    # Add resource for SDKMAN version - useful for basic connectivity testing
    @server.resource("sdkman://version")
    def get_sdkman_version() -> str:
        """Get SDKMAN version information."""
        result = sdk_version()
        if result["success"]:
            return result["data"]
        else:
            return f"Error getting SDKMAN version: {result.get('error', 'Unknown error')}"
    
    # Add resource for current SDKs
    @server.resource("sdkman://current")
    def get_current_sdks() -> str:
        """Get information about currently active SDKs."""
        result = sdk_current()
        if result["success"]:
            return result["data"]
        else:
            return f"Error getting current SDKs: {result.get('error', 'Unknown error')}"
    
    # Add resource for candidate versions
    @server.resource("sdkman://candidates/{candidate}")
    def get_candidate_versions(candidate: str) -> str:
        """Get available versions for a specific candidate."""
        result = sdk_list_candidate(candidate)
        if result["success"]:
            return result["data"]
        else:
            return f"Error getting versions for {candidate}: {result.get('error', 'Unknown error')}"
    
    return server 