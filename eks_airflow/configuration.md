[back to Readme](https://github.com/JC3008/DataEngineering_Kubernetes/blob/dev/Readme.md)
# IDE config
The cloud9 IDE was chosen as enviroment to set eks cluster up. It is nice to keep in mind that cloud9 is not for free, so be sure of setting up the timeout to 30 minutes which is the minimum timeout available. Although it is paid tool, it is low cost and we can take advantage of having an easier way of setting eks and airflow up.

## VPC and subnets
As cloud9 runs on EC2 instance, you'll need a subnet to emsemble it. If you don't have one, read the following steps.
### VPC
Is a resource isolation protocol tha allows us to run our apps safetly. It is mandatory that a VPC is builded under a given region.

### Creating a new VPC
* Give it a name
* Type a CIDR block (**I.E: 10.0.0.0/16**)
* Choose "Not work with ipv6"
* click on create
Check your recent created VPC on "your vpcs". <br>
 ***Note that this steps have been set manually, but it can be done using IAC.***
### Subnets
* Subnets (You can create private and public subnets)

## Cloud9
* Search for "cloud9" on AWS searching box
* Click on "new enviroment".
* Give it a name and select the following options:
![Alt text](https://github.com/JC3008/DataEngineering_Kubernetes/blob/dev/eks_airflow/images/cloud9.png)


