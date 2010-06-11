Name: pianobar
Version: 2010.6.1
Release: 1%{?dist}
Summary: "pianobar" is a free/open-source, console-based replacement for pandora's flash player.

Group: Applications/Multimedia
License: AS-IS
URL: http://6xq.net/html/00/17.html
Source0: http:/download.github.com/pianobar-2a1e819.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: cmake, libao-devel, libxml2-devel, faad2-libs
Requires: libao, faad2-libs, libxml2

%description
 "pianobar" supports all important features pandora has:
 * Create, delete, rename stations and add more music
 * Rate and temporary ban tracks as well as move them to another station
 * "Shared stations"
 * last.fm scrobbling
 * Proxy support for non-americans

%build
%cmake .
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
ctest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
