import argparse
import requests
import sys

def get_digest_and_tags(image_name, target_tag, registry_type):
    
    if registry_type == "dockerhub":
        return get_digest_and_tags_docker_hub(image_name, target_tag)
    else:
        raise ValueError(f"Invalid registry type: {registry_type}")

def get_digest_and_tags_docker_hub(image_name, target_tag):
    url_tag = f"https://hub.docker.com/v2/repositories/library/{image_name}/tags/{target_tag}/"
    response = requests.get(url_tag)
    tag_info = response.json()
    digest = tag_info.get('images', [{}])[0].get('digest')

    if not digest:
        raise ValueError(f"Error obtaining digest for tag {target_tag}.")

    url_tags = f"https://hub.docker.com/v2/repositories/library/{image_name}/tags/?page_size=100"
    response_tags = requests.get(url_tags)
    tags_info = response_tags.json()

    matching_tags = [result['name'] for result in tags_info.get('results', []) if result.get('images', [{}])[0].get('digest') == digest]

    return digest, matching_tags

def main():
    parser = argparse.ArgumentParser(description="Get digest and associated tags for an image and a specific tag.")
    parser.add_argument("image_name", help="Name of the image")
    parser.add_argument("target_tag", help="Specific tag of the image")
    parser.add_argument("--registry_type", choices=["dockerhub"], default="dockerhub", help="Type of registry")
    
    args = parser.parse_args()

    try:
        digest, matching_tags = get_digest_and_tags(args.image_name, args.target_tag, args.registry_type)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"Digest for tag {args.target_tag}: {digest}")
    print("Tags associated with the same digest:")
    for tag in matching_tags:
        print(tag)

if __name__ == "__main__":
    main()

