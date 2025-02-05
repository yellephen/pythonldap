import ldap3
import argparse
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--target', help="target ip address")
	parser.add_argument('-d','--domain', help="Domain DN eg. 'DC=test,DC=local'")
	parser.add_argument('-u','--username', help="users username, no domain. eg. administrator")
	parser.add_argument('-p','--password', help="users password")
	parser.add_argument('-U','--usertoadd', help="DN of the user")
	parser.add_argument('-G','--targetgroup', help="DN of the group")

	
	args = parser.parse_args()
	
	server = ldap3.Server(args.target, get_info = ldap3.ALL, port =389, use_ssl = False)
	connection = ldap3.Connection(server,args.username,args.password)
	connection.bind()
	addUsersInGroups(connection, args.usertoadd, args.targetgroup)
	#print the user to see if it worked
	searchFilter = "(DN="+args.usertoadd+")"
	print(searchFilter)
	connection.search(search_base=args.domain, search_filter=args.ldapfilter, search_scope='SUBTREE', attributes='*')
	print(connection.entries)

if __name__ == "__main__":
    main()

