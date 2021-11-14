This is the branch for handson on aws iam - to create groups, assign permissions, add users, create roles with best practices
To go through the best practices refer aws documentation. Some of them are
-- Using MFA on root account
-- Using groups with permissions and then adding users to it
-- not using inline policies much
-- using password rotation policy 
-- not sharing unnecessary priviliges - follow granting the least privilige method
-- giving programmatic access to those users who need, and same for console access
-- using Access analyzer to see which services are used mostly and refining the policies accordingly
-- not sharing the root user keys - access and secret ID - infact deleting it
-- not using root user for everyday tasks  - delegating it through roles - 
-- and having another IAM user with adminstrative privileges for aws admin tasks
-- not sharing access keys and secret keys among users - encrypting these keys on ur device - and using roles instead

AND most importantly doing your best each day and everyday !!! :) 

(later on this branch may be just chnaged to one dev branch)
(once confirmed and satisified witht he code, the code will be merged into the main branch)