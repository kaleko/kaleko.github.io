For the kaleko.github.io repository, use the MASTER branch instead of the gh-pages
When a repository is named specifically "username.github.io" the master branch
is the one that should have index.html, etc.
The "sources" for the site are stored on the sources branch.
Develop on the sources branch.

Compile the site with: 
>> make html

To publish, do:
>> ghp-import -b master output
>> git push origin master
