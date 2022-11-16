from sqlalchemy.orm import Session

# import crud
# import schemas
# import constants


# def init_db(db: Session) -> None:
#     """
#     Initialize the database with some default values.
#     """
#     # Create the default user
#     user = crud.user.get_by_email(db, email=constants.FIRST_SUPERUSER)
#     if not user:
#         user_in = schemas.UserCreate(
#             email=constants.FIRST_SUPERUSER,
#             password=constants.FIRST_SUPERUSER_PASSWORD,
#             is_superuser=True,
#         )
#         user = crud.user.create(db, obj_in=user_in)

