# docker_tag_tracker

*Docker Tag Tracker* is a simple Python script that allows you to retrieve the digest and associated tags for a specific tag of a Docker image. Currently, it supports querying images from Docker Hub.

## Usage

```bash
python docker_tag_tracker.py <image_name> <target_tag> [--registry_type {dockerhub}]
```
## Arguments

- <image_name>: Name of the Docker image.
- <target_tag>: Specific tag of the Docker image.
- --registry_type: Type of registry. Currently, only Docker Hub is supported.

## Example

```bash
python docker_tag_tracker.py nginx mainline-alpine
```

## Dependencies

- argparse: For parsing command line arguments.
- requests: For making HTTP requests to Docker Hub.

## How It Works

The script queries Docker Hub to obtain the digest associated with the specified tag. It then searches for all tags associated with the same digest, providing a comprehensive list of tags related to the specified Docker image.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Any feedback is highly appreciated!

## Author

Federico Abihaggle

## Acknowledgments

Special thanks to the Docker and Python communities for providing excellent tools and documentation.


