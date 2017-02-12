from sys import argv
import rpm

filename = argv[1]
rpm_file = open(filename)
ts = rpm.TransactionSet()
package = ts.hdrFromFdno(rpm_file)

print(package[rpm.RPMTAG_RELEASE])

rpm_file.close()

