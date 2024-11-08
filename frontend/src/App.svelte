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
  <style>
	/* Basic reset */
	* {
	  margin: 0;
	  padding: 0;
	  box-sizing: border-box;
	  font-family: Arial, sans-serif;
	}
  
	/* Main container styling */
	table {
	  width: 100%;
	  border-collapse: collapse;
	  margin: 20px 0;
	  font-size: 0.9rem;
	  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
	}
  
	/* Table header styling */
	thead th {
	  background-color: #f4f4f4;
	  color: #333;
	  padding: 12px;
	  text-align: left;
	  font-weight: 600;
	  border-bottom: 2px solid #ddd;
	}
  
	/* Table body styling */
	tbody tr {
	  border-bottom: 1px solid #eee;
	}
  
	tbody tr:nth-child(even) {
	  background-color: #f9f9f9;
	}
  
	tbody td {
	  padding: 12px;
	  color: #555;
	}
  
	/* Link styling */
	a {
	  color: #1a73e8;
	  text-decoration: none;
	  font-weight: 500;
	}
  
	a:hover {
	  text-decoration: underline;
	}
  
	/* Table cell alignment */
	td, th {
	  vertical-align: middle;
	}
  
	/* Table cell alignment and width for specific columns */
	th, td:nth-child(3),
	th:nth-child(3),
	td:nth-child(4),
	th:nth-child(4),
	td:nth-child(5),
	th:nth-child(5),
	td:nth-child(6),
	th:nth-child(6),
	td:nth-child(7),
	th:nth-child(7) {
	  text-align: center;
	}
  
	/* Highlight API Available cells */
	td:last-child {
	  font-weight: bold;
	  color: #00796b;
	}
  
	/* Error message styling */
	p {
	  color: #e53935;
	  font-size: 1.1rem;
	  margin: 20px 0;
	}
  </style>
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
  