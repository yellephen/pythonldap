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
	
	args = parser.parse_args()
	
	server = ldap3.Server(args.target, get_info = ldap3.ALL, port =389, use_ssl = False)
	connection = ldap3.Connection(server,args.username,args.password)
	connection.bind()
	
	searchFilter = "(objectClass=group)"
	connection.search(search_base=args.domain, search_filter=searchFilter, search_scope='SUBTREE', attributes='distinguishedName')
	print(connection.entries)
	for entry in connection.entries:
		entry=str(entry)
		endIndex = entry.index(" - STATUS")
		groupDN = entry[4:endIndex]
		print("Attempting to add to the following group:")
		print(groupDN)
		addUsersInGroups(connection, args.usertoadd, groupDN)
	#print the user to see if it worked
	print("Printing user to see if any worked")
	searchFilter = "(distinguishedName="+args.usertoadd+")"
	connection.search(search_base=args.domain, search_filter=searchFilter, search_scope='SUBTREE', attributes='*')
	print(connection.entries)

if __name__ == "__main__":
    main()

