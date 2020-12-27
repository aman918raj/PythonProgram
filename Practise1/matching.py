import fnmatch

ftp_evnt_fdbk_file = '202002_XGB.event'
ftp_evnt_fdbk_file_pattern = '20*.event'

res = fnmatch.fnmatch(ftp_evnt_fdbk_file, ftp_evnt_fdbk_file_pattern)
pr