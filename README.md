"# Fast-Build" 

API Docs:
## Base URL:http://localhost:8000/api
## Authentication:
**Type**:Token Authentication
**Header**(for authenticated endpoints): Authorization: Token <your_token_here>
---

## End Points:

### 1. Login

| Property           | Value                                         |
|--------------------|-----------------------------------------------|
| **URL**            | `/auth/login/`                                |
| **Method**         | `POST`                                        |
| **Authentication** | Not Required                                  |
| **Content-Type**   | `application/json`                            |
| **Description**    | `Log in with username or email and password.` |

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
| **400 Bad Request** | `{ "password": ["This Failed is required."] }`                             |
| **400 Bad Request** | `{ "non_Failed_errors": ["Unable to log in with provided credentials."] }` |



### 2. Logout

| Property           | Value                                         |
|--------------------|-----------------------------------------------|
| **URL**            | `/auth/logout/`                               |
| **Method**         | `POST`                                        |
| **Authentication** | Required                                      |
| **Content-Type**   | null                                          |
| **Description**    | `Log out from current user`                   |

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
| **400 Bad Request** | `{"non_Failed_errors": ["The two password Faileds didn't match."]}`         |
| **400 Bad Request** | `{"username": ["This Failed is required."]}`                               |
| **400 Bad Request** | `{"email": ["This Failed is required."]}`                                  |
| **400 Bad Request** | `{"password1": ["This Failed is required."]}`                              |
| **400 Bad Request** | `{"password2": ["This Failed is required."]}`                              |


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
| **400 Bad Request** | `{"new_password2": ["The two password Faileds didn’t match."]}`                            |
| **400 Bad Request** | `{"old_password": ["This Failed is required."]}`                                           |
| **400 Bad Request** | `{"new_password1": ["This Failed is required."]}`                                          |
| **400 Bad Request** | `{"new_password2": ["This Failed is required."]}`                                          |



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
| **400 Bad Request** | `{"non_Failed_errors": ["Incorrect input. access_token or code is required."]}`            |



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
| **200 OK**          | `{"status": "Failed","compitability": "Undefined","message": "..."}`                      |
| **200 OK**          | `{"status": "Success","compitability": "Danger","message": "..."}`                       |
| **200 OK**          | `{"status": "Success","compitability": "Warning","message": "..."}`                      |
| **200 OK**          | `{"status": "Success","compitability": "Success","message": "..."}`                      |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                                            |


#### notes



    -in Json request body:
        --the general form is :
        [[<part_id>,<number_of_piece>],...]
        --the user can add as much as he want from parts


    -in response message:
    --"status":Represent the status of Cart(normal Cart/PC Collection) and take values:
        --- "Failed": it is normal Cart
        --- "Success": it is Pc Collection
    
    --"compitability":Represent the status of PC parts compitability and take values:
        --- "Undefined": when it did not Represent a Pc Collection
        --- "Success": the parts should work togather
        --- "Warning": there is error in compitability but the collection still working
        --- "Danger": there is a massive error in compitability that would make the collection can not working

    --"message":Represent a message text that well be shown to the user to explane the status for so many conditions




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
| **200 OK**          | `{"status":"failed","message":"..."`                                                     |
| **200 OK**          | `{"status": "success","message":"..."`                                                   |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                                            |



#### notes

    -in Json request body:
        --the general form is :
        [[<part_id>,<number_of_piece>,is_discounted(0,1)],...]
        --the user can add as much as he want from parts
        --the usage of is_discounted value is to make sure that yhe order will done in tha same priece that the user see (so if some discount getting not valid before the user do the order the server will warning him that there is invalid discount in your order),take value 0 if the app did not find a discount for wanted piece and 1 if there was one


    -in response message:
        --"status":Represent the status of the function and take values:
            --- "failed": there was an error that prevent the server from post the order(as example the user order unvalid discount,shortage of one pieces in storage,or invalid part_id)
            --- "success": your order posted successfully
    
        --"message":Represent a message text that well be shown to the user to explane the status for so many conditions



## 10. order list

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/Cart/My-Orders/`                                                   |
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
| **URL**            | `/Cart/My-Orders/<cart_id>`                                          |
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
                        "id": 3,
                        "name": "sstey",
                        "price": 4345.0,
                        "image_filename": null
                    },
                    "quantity": 1
                },
                {
                    "part_detail": {
                        "id": 4,
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

## 13. Part Details

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/home/Parts/<int:id>`                                               |
| **Method**         | `GET`                                                                |
| **Authentication** | Required                                                             |
| **Content-Type**   | null                                                                 |
| **Description**    | `get Details of the wanted Part`                                     | 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                    |
|---------------------|-------------------------------------------------------------------------|
| **200 OK**          | `<wanted object>`                                                       |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                          |



## 14. Liked Part List

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/home/Like/List`                                                    |
| **Method**         | `GET`                                                                |
| **Authentication** | Required                                                             |
| **Content-Type**   | null                                                                 |
| **Description**    | `get list of parts that the user marked it`                          | 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                    |
|---------------------|-------------------------------------------------------------------------|
| **200 OK**          | `<list of objects>`                                                     |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                          |


### notes
    -objects list is like:
        [
            {
                "part": {
                    "id": 4,
                    "name": "zthsy",
                    "price": 567.0,
                    "population": 9,
                    "like_count": 1,
                    "image_filename": null
                },
                "created_at": "2025-05-06T06:04:56.145540Z"
            },...
        ]



## 15. put like

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/home/Like/put`                                                     |
| **Method**         | `POST`                                                               |
| **Authentication** | Required                                                             |
| **Content-Type**   | Content-Type                                                         |
| **Description**    | `add like for current user on wanted part`                           | 

#### Request Body

```json
{"part":4}
```

#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **201 Created**     | `<like object>`                                                           |
| **400 Bad Request** | `{"non_field_errors": ["The fields user, part must make a unique set."]}` |
| **400 Bad Request** | `{"part": ["This field is required."]}`                                   |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                            |


### notes
    -like object is like:
        {"id": 4,"created_at": "2025-05-06T06:04:56.145540Z","part": 4}

    -400 response reffered to that the user already had like on this part

## 16. remove like

| Property           | Value                                                                |
|--------------------|----------------------------------------------------------------------|
| **URL**            | `/home/Like/remove/<part_id>`                                        |
| **Method**         | `DELETE`                                                             |
| **Authentication** | Required                                                             |
| **Content-Type**   | null                                                                 |
| **Description**    | `remove like from current user on wanted part`                       | 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **204 No Content**  |                                                                           |
| **404 Not Found**   | `{"detail": "you don`t have like in this piece or it isn`t exist"}`       |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                            |


## 17. load Notifications

| Property           | Value                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------|
| **URL**            | `/home/Notification/Load`                                                                            |
| **Method**         | `GET`                                                                                                |
| **Authentication** | Required                                                                                             |
| **Content-Type**   | null                                                                                                 |
| **Description**    | `return list of notifications that related to user or public notification in dated order from newest`| 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **200 OK**          | `<list of notifications>`                                                 |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                            |

### notes
    -notifications list well be like:
        [
            {
                "id": 2,
                "type": "<Public/private>",
                "message": "test 2",
                "is_read": false,
                "created_at": "2025-05-06T05:20:13.801666Z"
            },...
        ]

## 18. mark Notifications as readed

| Property           | Value                            |
|--------------------|----------------------------------|
| **URL**            | `/home/Notification/Read/<id>`   |
| **Method**         | `POST`                           |
| **Authentication** | Required                         |
| **Content-Type**   | null                             |
| **Description**    | `mark a notification as readed`  | 

#### Request Body


#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **200 OK**          | `{"status": "Success"}`                                                   |
| **404 Not Found**   | `{"detail": "Notification not found"}`                                    |
| **403 Forbidden**   | `{"detail": "you have no permission on this notification"}`               |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                            |


## 19. Build PC

| Property           | Value                                                                     |
|--------------------|---------------------------------------------------------------------------|
| **URL**            | `/Build/build_pc/`                                                        |
| **Method**         | `POST`                                                                    |
| **Authentication** | Required                                                                  |
| **Content-Type**   | `application.json`                                                        |
| **Description**    | `api to help user building a bc depended on user budget and pc category`  | 

#### Request Body

```json
{
"budget":1200,
"pc_type":"Gaming",
"ordered_part":"powersupply",
"partList":[97,9,45,54,105,105,83,17,31]
}
```

#### Responses

| HTTP Status         | Body                                                                      |
|---------------------|---------------------------------------------------------------------------|
| **200 OK**          | `{"status": "<...>","query": [<part>,...],...`                            |
| **401 Unauthorized**| `{"detail": "Invalid token."}`                                            |
| **400 Bad Request** | `{"message":"error in part id list"}`                                     |
| **400 Bad Request** | `{"status": "failed","message":"some main parameters are missing,make sure to send all required parameters in json row body"}`                                     |


### notes

    -in request body:
        -budget: integer number represent user budget in dollar ($)
        -pc_type: take values: Gaming , Developer , Video Editing , Office
        -ordered_part: take values (prefer to pe in sort): motherboard , case , cpu , videocard , memory , internalharddrive , cpufan , casefan , powersupply
        - partList: is a list of  selected part id 


    -in 200 response the reterned data sa json is:
    |  key                  |   description                           |   Values                                                         |
    |-----------------------|-----------------------------------------|------------------------------------------------------------------|    
    | status                | the status of request                   | success , failed                                                 |    
    | query                 | filtered part from wanted part category | [{"id":<int>,"name": "<name of piece>","price": <float>,"population":<int>,"like_count":<int>,"image_filename":"<image path in server>"},...]                                                                |    
    | PC_class              | PC class depending on budget            | class A (recommended) , class B (requirement) , class C (weak)   |    
    | total_cost            | total cost of selected part             | float positive number                                            |
    | collection validation | is it a valid PC?                       | boolean value                                                    |
    | compatibility_status  | is all part compatible?                 | boolean value                                                    |
    | message               | report explain compatibility status     | string                                                           |
    | part_limit            | json data explane every type limit      | in next note                                                     |


    -'part_limit' values:
    | ordered_part value     | returned json                                        |
    |------------------------|------------------------------------------------------|
    | motherboard            | {'piece':1}                                          |
    | case                   | {'piece':1}                                          |
    | cpu                    | {'piece':1}                                          |
    | videocard              | {'piece':<integer>}                                  |
    | memory                 | {'piece':<integer>}                                  |
    | internalharddrive      | {'SATA':<integer>,'MVMe':<integer>,'m.2':<integer>}  |
    | cpufan                 | {'piece':1}                                          |
    | casefan                | {'fan_120mm':<integer>,'fan_140mm':<integer>}        |
    | powersupply            | {'piece':<0-1>}                                      |
