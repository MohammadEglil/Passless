# Contributing to the Cybersecurity Resource Database

# Contributing to the Cybersecurity Resource Database

Thank you for contributing! To add a new cybersecurity resource to our database, please follow the steps below.

## Steps to Submit a New Resource

1. **Fork the Repository**: Create a fork of this repository.
2. **Create a New File**: 
   - Add a new file in the `resources/` folder. The file should be in **YAML** or **JSON** format.
   - Name the file using the following convention: `resource_name.yaml` or `resource_name.json`.
3. **Follow the Template**: 
   - Use the provided template (`.github/RESOURCE_TEMPLATE.yaml` or `.github/RESOURCE_TEMPLATE.json`) to structure your data.
   - Make sure to fill in all required fields, marked with an asterisk (*).
4. **Submit a Pull Request**: After adding the resource, open a pull request with a clear title and description of the changes.

## Required Fields

Please fill in the following fields when submitting a new resource:

- **Resource Name**: The name of the cybersecurity tool/resource.
- **Type**: The type of resource (e.g., tool, blog, tutorial, etc.).
- **Link**: The URL to the resource.
- **Authority\***: The perceived authority or credibility of the source. (e.g., high, medium, low)
- **Popularity\***: Popularity level or usage (e.g., high, medium, low).
- **Category\***: The main category for the resource (e.g., threat intelligence, incident response, etc.).
- **Author**: The creator or maintainer of the resource (if applicable).
- **Last Updated**: The last update date of the resource.
- **Skill Level\***: The required skill level to use or understand the resource (e.g., beginner, intermediate, advanced).
- **Access**: Whether the resource is free, freemium, or paid.
- **Keywords\***: A list of relevant keywords for search optimization.
- **API**: Indicate if the resource has an API (e.g., true/false or provide API details if applicable).

## Example Pull Request

When submitting a pull request, make sure the description clearly explains the new resource and why it’s valuable to the community. You may also include relevant information such as the target audience and use cases.
