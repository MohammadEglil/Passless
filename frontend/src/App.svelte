<script>
	import { onMount } from 'svelte';
  
	let items = [];
	let error = null;
	// This function will fetch the data when the component mounts
	onMount(async () => {
	  try {
		const response = await fetch(`http://74.242.198.13/items`, {
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
  
	/* Page container */
	.container {
	  width: 90%;
	  max-width: 1200px;
	  margin: 40px auto;
	  text-align: center;
	}
  
	/* Header styling */
	header {
	  background-color: #00796b;
	  padding: 20px;
	  color: #fff;
	  border-radius: 8px;
	  margin-bottom: 30px;
	  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
	}
  
	header h1 {
	  font-size: 2rem;
	  font-weight: 700;
	}
  
	/* Responsive table container */
	.table-container {
	  overflow-x: auto; /* Horizontal scroll for small screens */
	}
  
	/* Table styling */
	table {
	  width: 100%;
	  border-collapse: collapse;
	  margin-top: 20px;
	  font-size: 0.9rem;
	  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
	  border-radius: 8px;
	  overflow: hidden;
	}
  
	/* Table header styling */
	thead th {
	  background-color: #f4f4f4;
	  color: #333;
	  padding: 15px;
	  text-align: left;
	  font-weight: 600;
	  border-bottom: 2px solid #ddd;
	}
  
	/* Table row styling */
	tbody tr {
	  border-bottom: 1px solid #eee;
	  transition: background-color 0.3s;
	}
  
	tbody tr:hover {
	  background-color: #f0f8ff;
	}
  
	tbody tr:nth-child(even) {
	  background-color: #fafafa;
	}
  
	/* Table data cell styling */
	tbody td {
	  padding: 15px;
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
  
	/* Center alignment for specific columns */
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
	.error {
	  color: #e53935;
	  font-size: 1.1rem;
	  margin: 20px 0;
	}
  
	/* Responsive styling for smaller screens */
	@media (max-width: 768px) {
	  /* Stack table in mobile-friendly format */
	  table, thead, tbody, th, td, tr {
		display: block;
	  }
  
	  thead {
		display: none;
	  }
  
	  tbody tr {
		margin-bottom: 15px;
		border: 1px solid #ddd;
		padding: 10px;
		border-radius: 8px;
	  }
  
	  tbody td {
		display: flex;
		justify-content: space-between;
		padding: 8px 0;
	  }
  
	  /* Label for each cell */
	  tbody td::before {
		content: attr(data-label);
		font-weight: bold;
		color: #333;
		text-align: left;
		flex-basis: 50%;
		padding-right: 10px;
	  }
	}
  </style>
  
  <div class="container">
	<!-- Header with title "Passless" -->
	<header>
	  <h1>Passless</h1>
	</header>
  
	<!-- Display error message or loading text -->
	{#if error}
	  <p class="error">Error loading data: {error}</p>
	{:else if items.length === 0}
	  <p>Loading...</p>
	{:else}
	  <!-- Responsive table container -->
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
				<td data-label="Link"><a href="{item.link}" target="_blank">Link</a></td>
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
  