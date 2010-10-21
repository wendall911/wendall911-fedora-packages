RPM Building instructions:

## Prereqs
$ yum groupinstall "Development Tools"
$ yum install rpmdevtools
$ rpmdev-setuptree

## Dependencies not in Fedora 13 or common alternative repos
$ wget http://dl.atrpms.net/f13-i386/atrpms/stable/faad2-devel-2.7-16.fc13.i686.rpm
$ rpm -ihv --nodeps faad2-devel-2.7-16.fc13.i686.rpm

## Build RPM
1. update PIANOBAR.spec with new version and source tarball name
2. Fetch source. Could use spectool here, but it's semi-broken rpm crap and path must 100% match the filename.
3. create source tarball and place in ~/rpmbuild/SOURCES/ (tar -cjf pianobar-{HEAD}.tar.gz BUILD/*)
4. cd ~/rpmbuild/SPECS/
5. $ rpmbuild -ba PIANOBAR.spec

Two rpm files are generated and placed into:
~/rpmbuild/RPMS/{arch}
~/rpmbuild/SRPMS/

To install
rpm -ihv pianobar-2010.6.1-1.fc13.i686.rpm
