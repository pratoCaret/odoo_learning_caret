# Stash Changes:
git stash

This saves the current modifications and reverts the working directory to the last committed state.

# List Stashes:
git stash list

Displays all stashed changes.

# Apply Stashed Changes:
git stash apply

Applies the most recent stash without removing it from the stash list.

# Apply and Remove Stash:
git stash pop

Applies the most recent stash and removes it from the stash list.

# Apply Specific Stash:
git stash apply stash@{n}

Applies a specific stash (replace n with the stash index from git stash list ).

# Delete a Specific Stash:
git stash drop stash@{n}

Deletes a specific stash.

# Clear All Stashes:
git stash clear

Removes all stashed changes.
