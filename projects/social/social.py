import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0    
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1                                                # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

# !!!! IMPLEMENT ME
# Add users
        for i in range(0, num_users):
            self.add_user(f'User{i}')
        new_friendships = []                                       #creae friendship, and all possible combinations.
        for user_id in self.users:                                      #Avoid duplicates by ensuring 
            for friend_id in range(user_id + 1, self.last_id + 1):
                new_friendships.append((friend_id, user_id))
        random.shuffle(new_friendships)                            #Random the new possible friendships.
        averag = num_users * avg_friendships//2
        for i in range(averag):
            friendship = new_friendships[i]
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}                                                   #dictionary
        results = {}                                                   
        for contact_id in self.users:
            visited[contact_id] = []
            queue = []
            queue.append([contact_id])
            network_len = len(results)
            while len(queue) > 0:
                path = queue.pop(0)
                y_contact_id = path[-1]
                if y_contact_id not in visited[contact_id]:
                    visited[contact_id].append(y_contact_id)
                if y_contact_id == user_id:
                    path.reverse()
                    results[contact_id] = path                           # connection found
                    break                                               # connecting to the next person
                for friend_id in self.friendships[y_contact_id]:
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    queue.append(path_copy)
        if len(results) == network_len:                                 # if not added then no was found
            print("No Connection found: " + str(person_id))

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
