## nucleihub-templates

This repo collects nuclei template from 600+ github repos, updates every 12 hours.

## These Steps are only for github-actions
```
# Step 1
curl -s "https://raw.githubusercontent.com/rix4uni/nucleihub/refs/heads/main/reponames.txt" | nucleihub updatecheck | grep "Updated today:" | sed 's/^\Updated today: //' | nucleihub download --output-directory nucleihub-downloaded-repos

# Step 2
nucleihub duplicate --input-directory nucleihub-downloaded-repos --output-directory nucleihub-templates --large-content

# Step 3
find nucleihub-templates -mindepth 1 -maxdepth 1 -exec mv -t . {} + && rm -rf nucleihub-downloaded-repos nucleihub-templates
```
