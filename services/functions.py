from models.models import Followers
from conections.mysql import conection_userprofile

def unfollow_user(id_follower, id_following):
    session = conection_userprofile()

    if id_follower == id_following:
        return {"error": "You cannot unfollow yourself"}, 400

    follow_relation = session.query(Followers).filter_by(
        Id_Follower=id_follower,
        Id_Following=id_following,
        Status=1
    ).first()

    if not follow_relation:
        session.close()
        return {"error": "Follow relationship not found or already inactive"}, 404

    follow_relation.Status = 0
    session.commit()
    session.close()
    return {"message": "Unfollowed successfully"}, 200
