## Helpful python cdk repo

### Prerequisites

### Run via Docker

```
docker compose build cdk_dev
docker compose run cdk_dev
```

### Start using cdk

In an empty directory, run:

```
cdk init app --language python
```

#### account

To use ENV variables

```
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-east-1
```

Switch account on cdk use

```
cdk deploy --profile aws_main
```

### Destroy a stack

```
cdk destroy --profile aws_main
```
