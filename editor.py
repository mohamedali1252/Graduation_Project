import sys
import time
import os

def edit_features():
	connections = []
	connections_after = []
	connections_count = 0
	
	if len(sys.argv) != 2:
		return 1
	else:
		read = sys.argv[1]
		file_csv = open(read, "r")
		for x in file_csv:
			connections.append(x)
			connections_count = connections_count + 1
		file_csv.close()
		for counter in range(0,connections_count):
			line1 = connections[counter]
			sep_conn = line1.split(",")
			conn_no = sep_conn[0]
			start_time = sep_conn[1]
			orig_p = sep_conn[2]
			resp_p = sep_conn[3]
			orig_h = sep_conn[4]
			resp_h = sep_conn[5]
			duration = sep_conn[6]
			protocol = sep_conn[7]
			service = sep_conn[8]
			unknown = sep_conn[9]
			flag = sep_conn[10]
			src_bytes = sep_conn[11]
			dst_bytes = sep_conn[12]
			land = sep_conn[13]
			wrong_fragment = sep_conn[14]
			urgent = sep_conn[15]
			
			total = float(start_time) + 6*60*60 + float(duration)
			t  = time.localtime(total)
			time_string = time.strftime("[%d/%b/%Y %H:%M:%S]", t)
			
			hot = sep_conn[16]
			num_failed_logins = sep_conn[17]
			logged_in= sep_conn[18]
			num_compromised=sep_conn[19]
			root_shell = sep_conn[20]
			su_attempted = sep_conn[21]
			num_root = sep_conn[22]
			num_file_creations = sep_conn[23]
			num_shells = sep_conn[24]
			num_access_files = sep_conn[25]
			num_outbound_cmds = sep_conn[26]
			is_hot_login = sep_conn[27]
			is_guest_login = sep_conn[28]
			
			if service =="ssh" or resp_p=="22" :
				file_ssh = open("ssh.log", "r")
				for x in file_ssh:
#[date time] src_ip src_port dst_ip dst_port,hot,num_failed_login,logged_in,num_compromised_file,root_shell,su_attempted,num_root,num_file_creations,num_shells,num_access_files,num_outbound_cmds,is_hot_login,is_guest_login 
					if  (time_string in x) and (orig_h in x) and  (orig_p in x) and (resp_h in x) and (resp_p in x):
						print ("found one")
						ssh = x.split(",")
						hot = ssh[1]
						num_failed_logins = ssh[2]
						logged_in= ssh[3]
						num_compromised=ssh[4]
						root_shell = ssh[5]
						su_attempted = ssh[6]
						num_root = ssh[7]
						num_file_creations = ssh[8]
						num_shells = ssh[9]
						num_access_files = ssh[10]
						num_outbound_cmds = ssh[11]
						is_hot_login = ssh[12]
						is_guest_login = ssh[13]
						line2 = duration + "," + protocol + "," +"ssh"+ "," + flag + ","+ src_bytes + ","+ dst_bytes + ","+land+ ","+wrong_fragment+ ","+urgent+ "," +hot+ "," +num_failed_logins+ "," +logged_in+ "," +num_compromised+ "," +root_shell+ "," +su_attempted+ "," +num_root+ "," +num_file_creations+ "," +num_shells+ "," +num_access_files+ "," +num_outbound_cmds+ "," +is_hot_login+ "," +is_guest_login+ "," + sep_conn[29] +","+sep_conn[30] + "," +sep_conn[31]+ ","+ sep_conn[32] +","+ sep_conn[33] +","+sep_conn[34] +","+sep_conn[35] +","+sep_conn[36] +","+sep_conn[37]+ ","+sep_conn[38]+ ","+sep_conn[39]+ ","+sep_conn[40]+ ","+sep_conn[41]+ ","+sep_conn[42]+ ","+sep_conn[43]+ ","+sep_conn[44] +","+ sep_conn[45] +","+ sep_conn[46] +","+ sep_conn[47].rstrip()
						connections_after.append(line2)
			
			
			
			elif service == "ftp" or resp_p=="21":
				print("Nothing to do")
			
			
			
			elif service =="smtp" or resp_p=="25":
						line2 = duration + "," + protocol + "," +"ssh"+ "," + flag + ","+ src_bytes + ","+ dst_bytes + ","+land+ ","+wrong_fragment+ ","+urgent+ "," +hot+ "," +num_failed_logins+ "," +logged_in+ "," +num_compromised+ "," +root_shell+ "," +su_attempted+ "," +num_root+ "," +num_file_creations+ "," +num_shells+ "," +num_access_files+ "," +num_outbound_cmds+ "," +is_hot_login+ "," +is_guest_login+ "," + sep_conn[29] +","+sep_conn[30] + "," +sep_conn[31]+ ","+ sep_conn[32] +","+ sep_conn[33] +","+sep_conn[34] +","+sep_conn[35] +","+sep_conn[36] +","+sep_conn[37]+ ","+sep_conn[38]+ ","+sep_conn[39]+ ","+sep_conn[40]+ ","+sep_conn[41]+ ","+sep_conn[42]+ ","+sep_conn[43]+ ","+sep_conn[44] +","+ sep_conn[45] +","+ sep_conn[46] +","+ sep_conn[47].rstrip()
		
		
		file_after = open("formated.txt", "w")	
		for i in range(0,len(connections_after)):
			file_after.write(connections_after[i])
		file_after.close()
			
			
			
			
edit_features()				