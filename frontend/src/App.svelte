<script>
	import { onMount } from 'svelte';
	let items = [];
	let error = null;
	let searchQuery = ''; // To hold the user's search input
	let isLoading = false;

	// Function to fetch items, using /items for no search query
	async function fetchItems(query = '') {
		try {
			isLoading = true;
			const url = query
				? `http://4.226.1.49/search?query=${encodeURIComponent(query)}`
				: `http://4.226.1.49/items`; // Use /items when no search query
			const response = await fetch(url, {
				headers: {
					'Accept': 'application/json',
				},
			});

			if (!response.ok) {
				throw new Error('Failed to fetch data');
			}

			const data = await response.json();
			items = data.items || data.results; // Use items from /items or results from /search
			error = null;
		} catch (err) {
			error = err.message;
			items = [];
		} finally {
			isLoading = false;
		}
	}

	// Fetch all items on mount
	onMount(async () => {
		await fetchItems();
	});

	// Triggered when the user submits a search
	function handleSearch() {
		fetchItems(searchQuery);
	}
</script>


<style>
	/* Add styling for the search bar and button */
	.search-container {
		margin: 20px auto;
		text-align: center;
	}

	.search-container input[type="text"] {
		width: 60%;
		padding: 10px;
		font-size: 1rem;
		border: 1px solid #ddd;
		border-radius: 4px;
	}

	.search-container button {
		padding: 10px 20px;
		font-size: 1rem;
		background-color: #00796b;
		color: #fff;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		margin-left: 10px;
	}

	.search-container button:hover {
		background-color: #005a4c;
	}
</style>

<div class="container">
	<header>
		<h1>Passless</h1>
	</header>

	<!-- Search bar -->
	<div class="search-container">
		<input
			type="text"
			placeholder="Search for resources..."
			bind:value="{searchQuery}" />
		<button on:click="{handleSearch}">Search</button>
	</div>

	<!-- Display error message, loading text, or the table -->
	{#if error}
		<p class="error">Error loading data: {error}</p>
	{:else if isLoading}
		<p>Loading...</p>
	{:else if items.length === 0}
		<p>No results found.</p>
	{:else}
		<div class="table-container">
			<table>
				<thead>
					<tr>
						<th>ID</th>
						<th>Resource Name</th>
						<th>Type</th>
						<th>Link</th>
						<th>Authority</th>
						<th>Popularity</th>
						<th>Category</th>
						<th>Author</th>
						<th>Last Updated</th>
						<th>Skill Level</th>
						<th>Access</th>
						<th>Keywords</th>
						<th>API Available</th>
					</tr>
				</thead>
				<tbody>
					{#each items as item}
						<tr>
							<td data-label="ID">{item.id}</td>
							<td data-label="Resource Name">{item.resource_name}</td>
							<td data-label="Type">{item.type}</td>
							<td data-label="Link">
								<a href="{item.link}" target="_blank">Link</a>
							</td>
							<td data-label="Authority">{item.authority}</td>
							<td data-label="Popularity">{item.popularity}</td>
							<td data-label="Category">{item.category}</td>
							<td data-label="Author">{item.author}</td>
							<td data-label="Last Updated">{item.last_updated}</td>
							<td data-label="Skill Level">{item.skill_level}</td>
							<td data-label="Access">{item.access}</td>
							<td data-label="Keywords">{item.keywords}</td>
							<td data-label="API Available">{item.api_available}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
</div>
