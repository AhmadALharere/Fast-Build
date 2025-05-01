"# Fast-Build" 

API Docs:
## Base URL:http://localhost:8000/api
## Authentication:
    -**Type**:Token Authentication
    - **Header**(for authenticated endpoints): Authorization: Token <your_token_here>
---

## End Points:

### 1. Login

| Property           | Value                                         |
|--------------------|-----------------------------------------------|
| **URL**            | `/auth/login/`                                |
| **Method**         | `POST`                                        |
| **Authentication** | Not Required                                  |
| **Content-Type**   | `application/json`                            |
| **Description**    | Log in with username or email and password.   |

#### Request Body

```json
either
{ "username": "newuser", "password": "srhjg" }
or
{ "email": "newuser@gmail.com", "password": "srhjg" }
```
#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **200 OK**          | `{ "key": "a7ca******..." }`                                              |
| **400 Bad Request** | `{ "password": ["This field is required."] }`                             |
| **400 Bad Request** | `{ "non_field_errors": ["Unable to log in with provided credentials."] }` |



### 2. Logout

| Property           | Value                                         |
|--------------------|-----------------------------------------------|
| **URL**            | `/auth/logout/                                |
| **Method**         | `POST`                                        |
| **Authentication** | Required                                      |
| **Content-Type**   | null                                          |
| **Description**    | Log out from current user                     |

#### Request Body

null

#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **200 OK**          | `{"detail": "Successfully logged out."}`                                  |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                            |


### 3. Registration

| Property           | Value                                         |
|--------------------|-----------------------------------------------|
| **URL**            | `/auth/registration/`                         |
| **Method**         | `POST`                                        |
| **Authentication** | Not Required                                  |
| **Content-Type**   | `application/json`                            |
| **Description**    | signup                                        |

#### Request Body

```json
{"username": "newuser","email": "newuser@example.com","password1": "aeamlgng","password2": "aeamlgng"}
```
#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **204 No Content**  |                                                                           |
| **400 Bad Request** | `{"username": ["A user with that username already exists."]}`             |
| **400 Bad Request** | `{"email": ["Email is already in use."]}`                                 |
| **400 Bad Request** | `{"non_field_errors": ["The two password fields didn't match."]}`         |
| **400 Bad Request** | `{"username": ["This field is required."]}`                               |
| **400 Bad Request** | `{"email": ["This field is required."]}`                                  |
| **400 Bad Request** | `{"password1": ["This field is required."]}`                              |
| **400 Bad Request** | `{"password2": ["This field is required."]}`                              |


### 4. Change Password

| Property           | Value                                                          |
|--------------------|----------------------------------------------------------------|
| **URL**            | `/auth/password/change/`                                       |
| **Method**         | `POST`                                                         |
| **Authentication** | Required                                                       |
| **Content-Type**   | `application/json`                                             |
| **Description**    | `change password for current user account without logging out` |

#### Request Body

```json
{"old_password": "stlhks","new_password1": "NewPassword","new_password2": "NewPassword"}
```
#### Responses

| HTTP Status         | Body                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| **200 OK**          | `{"detail": "New password has been saved."}`                                              |
| **400 Bad Request** | `{"old_password": ["Your old password was entered incorrectly. Please enter it again."]}` |
| **400 Bad Request** | `{"new_password2": ["The two password fields didn’t match."]}`                            |
| **400 Bad Request** | `{"old_password": ["This field is required."]}`                                           |
| **400 Bad Request** | `{"new_password1": ["This field is required."]}`                                          |
| **400 Bad Request** | `{"new_password2": ["This field is required."]}`                                          |



### 5. Log in/sign up with Google

| Property           | Value                                                          |
|--------------------|----------------------------------------------------------------|
| **URL**            | `/auth/user/google/`                                           |
| **Method**         | `POST`                                                         |
| **Authentication** | Not Required                                                   |
| **Content-Type**   | `application/json`                                             |
| **Description**    | `Log in or Sign up for google accounts`                        |

#### Request Body

```json
{"access_token":"***.....","provider":"google"}
```
#### Responses

| HTTP Status         | Body                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| **200 OK**          | `{"key": "********..."}`                                                                  |
| **401 Unauthorized**| `{"detail": "Invalid Google access token."}`                                              |
| **400 Bad Request** | `{"non_field_errors": ["Incorrect input. access_token or code is required."]}`            |



### 6. Get proflie

| Property           | Value                                                          |
|--------------------|----------------------------------------------------------------|
| **URL**            | `/auth/user/profile/`                                          |
| **Method**         | `GET`                                                          |
| **Authentication** | Required                                                       |
| **Content-Type**   | null                                                           |
| **Description**    | `get profile data for current user`                            |

#### Request Body


#### Responses

| HTTP Status         | Body                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| **200 OK**          |
`{"username": "..","email": "..","first_name": "..","last_name": "..","birth_date": "..","phone_number": "..","gender": "..","image": ".."}`|
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                                            |



### 7. Edit proflie

| Property           | Value                                                          |
|--------------------|----------------------------------------------------------------|
| **URL**            | `/auth/user/profile/`                                          |
| **Method**         | `PATCH`                                                        |
| **Authentication** | Required                                                       |
| **Content-Type**   | `application/json`                                             |
| **Description**    | `get profile data for current user`                            |

#### Request Body

```json
{"username": "ahmad","email": "ahmed@example.com","first_name": "أحمد","last_name": "الحريري","gender": "Male","birth_date":"2003-09-15","phone_number": "0954368434"}
```

#### Responses

| HTTP Status         | Body                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| **200 OK**          |
`{"username": "..","email": "..","first_name": "..","last_name": "..","birth_date": "..","phone_number": "..","gender": "..","image": ".."}`|
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                                            |




## 8. Check Cart

| Property           | Value                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------|
| **URL**            | `/Cart/Check-Cart`                                                                                |
| **Method**         | `POST`                                                                                            |
| **Authentication** | Required                                                                                          |
| **Content-Type**   | `application/json`                                                                                |
| **Description**    | `check if the user order a normal cart or PC collection then if it collection check compitapility`|

#### Request Body

```json
[[4,1],[3,1]]
```

#### Responses

| HTTP Status         | Body                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| **200 OK**          | `{"statues": "Field","compitability": "Undefined","massege": "..."}`                      |
| **200 OK**          | `{"statues": "Success","compitability": "Danger","massege": "..."}`                       |
| **200 OK**          | `{"statues": "Success","compitability": "Warning","massege": "..."}`                      |
| **200 OK**          | `{"statues": "Success","compitability": "Success","massege": "..."}`                      |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                                            |


#### notes



    -in Json request body:
        --the general form is :
        [[<part_id>,<number_of_piece>],...]
        --the user can add as much as he want from parts


    -in response message:
    --"statues":Represent the statues of Cart(normal Cart/PC Collection) and take values:
        --- "Field": it is normal Cart
        --- "Success": it is Pc Collection
    
    --"compitability":Represent the statues of PC parts compitability and take values:
        --- "Undefined": when it did not Represent a Pc Collection
        --- "Success": the parts should work togather
        --- "Warning": there is error in compitability but the collection still working
        --- "Danger": there is a massive error in compitability that would make the collection can not working

    --"massege":Represent a massege text that well be shown to the user to explane the statues for so many conditions




## 9. Order Cart

| Property           | Value                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
| **URL**            | `/Cart/order/`                                                                                                          |
| **Method**         | `POST`                                                                                                                  |
| **Authentication** | Required                                                                                                                |
| **Content-Type**   | `application/json`                                                                                                      |
| **Description**    | `post the cart then check if user order is posible(if there is enaugh piece,if piece_id is valied),then apply his order`|

#### Request Body

```json
[[4,1,0],[3,1,,0]]
```

#### Responses

| HTTP Status         | Body                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------|
| **200 OK**          | `{"statues":"failed","message":"..."`                                                     |
| **200 OK**          | `{"statues": "success","message":"..."`                                                   |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                                            |



#### notes

    -in Json request body:
        --the general form is :
        [[<part_id>,<number_of_piece>,is_discounted(0,1)],...]
        --the user can add as much as he want from parts
        --the usage of is_discounted value is to make sure that yhe order will done in tha same priece that the user see (so if some discount getting not valid before the user do the order the server will warning him that there is invalid discount in your order),take value 0 if the app did not find a discount for wanted piece and 1 if there was one


    -in response message:
        --"statues":Represent the statues of the function and take values:
            --- "failed": there was an error that prevent the server from post the order(as example the user order unvalid discount,shortage of one pieces in storage,or invalid part_id)
            --- "success": your order posted successfully
    
        --"massege":Represent a massege text that well be shown to the user to explane the statues for so many conditions



## 10. order list

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/Cart/My-Orders`                                                    |
| **Method**         | `GET`                                                                |
| **Authentication** | Required                                                             |
| **Content-Type**   | null                                                                 |
| **Description**    | `get list of all orders that the user has done start from newest one`|

#### Request Body


#### Responses

| HTTP Status         | Body                                                                    |
|---------------------|-------------------------------------------------------------------------|
| **200 OK**          | `<list of opjects>`                                                     |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                          |


#### notes

    -returned list contains object like:
        {
        "id": 17,
        "order_date": "2025-04-28T10:32:57.371369Z",
        "total_cost": 4912.0,
        "state": "Waiting"
        }
    -every objects represent a Cart




## 11. order details

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/Cart/My-Orders`                                                    |
| **Method**         | `GET`                                                                |
| **Authentication** | Required                                                             |
| **Content-Type**   | null                                                                 |
| **Description**    | `get details of the order`                                           | 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                    |
|---------------------|-------------------------------------------------------------------------|
| **200 OK**          | `<wanted object>`                                                       |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                          |
| **404 Not Found**   | `{"detail": "No ShopBasket matches the given query."}`                  |

#### notes

    -returned object like:
                {
            "id": 17,
            "order_date": "2025-04-28T10:32:57.371369Z",
            "total_cost": 4912.0,
            "state": "Waiting",
            "orders": [
                {
                    "part_detail": {
                        "Gid": 3,
                        "name": "sstey",
                        "price": 4345.0,
                        "image_filename": null
                    },
                    "quantity": 1
                },
                {
                    "part_detail": {
                        "Gid": 4,
                        "name": "zthsy",
                        "price": 567.0,
                        "image_filename": null
                    },
                    "quantity": 1
                }
                ]
            }
    -this api returned the object just if the user already had it so if someone try to inter id for Cart that he do not have he will get 404 response

    

## 12. Part List

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/home/Parts/`                                                       |
| **Method**         | `GET`                                                                |
| **Authentication** | Required                                                             |
| **Content-Type**   | null                                                                 |
| **Description**    | `get list of Parts with some filters`                                | 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                    |
|---------------------|-------------------------------------------------------------------------|
| **200 OK**          | `<list of object>`                                                      |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                          |


#### filters and search


| key       | type          | values                                                                                         |
|-----------|---------------|------------------------------------------------------------------------------------------------|
| part_type | filter        | `<name of categury in small-laters>`                                                           |
| min_price | filter        | `<float number>`                                                                               |
| max_price | filter        | `<float number>`                                                                               |
| page      | pagenator     | `<integer number>`                                                                             |
| ordering  | order method  | ` liked , population , price , date_created , -liked , -population , -price , -date_created `  |
| search    | search        | `<string>`                                                                                     |



#### notes

    -in filter.part_type, categury name is:
    'case','caseaccessory','casefan','cpu','cpucooler','motherboart','externalharddrive','internalharddrive','fancontroller','headphones','keyboard','memory','monitor','opticaldrive','mouse','powersupply','soundcard','speakers','thermalpaste','videocard','webcam','wiresnetworkcard','wirelessnetworkcard'
