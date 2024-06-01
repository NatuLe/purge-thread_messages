'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import interactions
# Use the following method to import the internal module in the current same directory

# Import the os module to get the parent path to the local files
import os
# aiofiles module is recommended for file operation
import aiofiles
# You can listen to the interactions.py event
from interactions.api.events import MessageCreate
# You can create a background task
from interactions import Task, IntervalTrigger

'''
Replace the ModuleName with any name you'd like
'''
class PurgeAllMessages(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="purge",
        description=" "
    )
    

    @module_base.subcommand("all the messages in threads", sub_cmd_description="Purge all messages of a user in a server")
    @interactions.slash_option(
        name = "member",
        description = "The member to purge messages of",
        required = True,
        opt_type = interactions.OptionType.USER
    )
    async def module_group_ping(self, ctx: interactions.SlashContext, member: str):
        if ctx.author.id!= 'your_user_id':
            await ctx.send("You are not authorized to use this command.",ephemeral=True)
            return
        # Get the guild object
        guild = ctx.guild
        
        
        
        await ctx.send(f"Purging all messages in the threads of {member.mention} in {guild.name}...",ephemeral=True)
        
        threads=guild.threads
        lock_status=False
        for thread in threads:
            if thread.locked:
                lock_status=True
                await thread.edit(locked=False)
            await thread.purge(limit=None, check=lambda m: m.author.id == member.id)
            if lock_status:
                await thread.edit(locked=True)
                lock_status=False
        
            
    
