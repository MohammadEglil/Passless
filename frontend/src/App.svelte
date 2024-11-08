<script>
	import { onMount } from 'svelte';
  
	let items = [];
	let error = null;
	// This function will fetch the data when the component mounts
	onMount(async () => {
	  try {
		const response = await fetch(`http://20.250.188.147/items`, {
		  headers: {
			'Accept': 'application/json',
		  },
		});
  
		if (!response.ok) {
		  throw new Error('Failed to fetch data');
		}
  
		const data = await response.json();
		items = data.items;
	  } catch (err) {
		error = err.message;
	  }
	});
  </script>
  
  <!-- HTML to display the fetched data -->
  {#if error}
	<p>Error loading data: {error}</p>
  {:else if items.length === 0}
	<p>Loading...</p>
  {:else}
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
			<td>{item.id}</td>
			<td>{item.resource_name}</td>
			<td>{item.type}</td>
			<td><a href="{item.link}" target="_blank">Link</a></td>
			<td>{item.authority}</td>
			<td>{item.popularity}</td>
			<td>{item.category}</td>
			<td>{item.author}</td>
			<td>{item.last_updated}</td>
			<td>{item.skill_level}</td>
			<td>{item.access}</td>
			<td>{item.keywords}</td>
			<td>{item.api_available}</td>
		  </tr>
		{/each}
	  </tbody>
	</table>
  {/if}
  