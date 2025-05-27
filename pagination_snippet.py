# Import the necessary library
from aihub import AIHub

# Initialize the AIHub client
# Replace with your actual API root, API token, and IB context
client = AIHub(
    api_root="<API-ROOT>",
    api_token="<API-TOKEN>",
    ib_context="<IB-CONTEXT>",
)

# Initialize an empty list to store all file results
all_files_results = []

# Initialize the starting offset for pagination
current_offset = 0

# Replace with your actual RUN ID
run_id = "<RUN-ID>"

# Loop to fetch all results using pagination
while True:
    # Fetch results with the current offset
    results = client.apps.runs.results(run_id, file_offset=current_offset)

    # Extend the list with the files from the current response
    all_files_results.extend(results.files)

    # Check if there are more results to fetch
    if not results.has_more:
        # If not, break the loop
        break

    # Increment the offset by the number of files received in the current response
    current_offset += len(results.files)

# Now, all_files_results contains all files from all pages
# You can then process the all_files_results list as needed
print(f"Successfully fetched {len(all_files_results)} files.")
