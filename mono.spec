# Based off of a spec file by Dag Wieers <dag@wieers.com>
# http://dag.wieers.com/packages/mono/mono.spec

Summary: Mono CIL runtime
Name: mono
Version: 1.1.3
Release: 1
URL: http://www.mono-project.com/
License: LGPL
Group: System Environment/Base
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: bison
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: pkgconfig
BuildRequires: icu
BuildRequires: libicu-devel
Requires: libicu
Requires: /sbin/ldconfig

%description
The Mono runtime implements a JIT engine for the ECMA CLI virtual
machine (as well as a byte code interpreter, the class loader, the
garbage collector, threading system and metadata access libraries).

%package devel
Summary: mono-devel
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries, and
development documentation for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

#%post
#echo "You must install libgdiplus separately."

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
#rm -rf $RPM_BUILD_ROOT%{_bindir}/gmcs
#rm -rf $RPM_BUILD_ROOT%{_libdir}/mono/2.0
#rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
#rm -rf $RPM_BUILD_ROOT%{_datadir}/libgc-mono
rm -rf $RPM_BUILD_ROOT/usr/man/*

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%doc %{_mandir}/man1/mcs.*
%doc %{_mandir}/man1/mono.*
%doc %{_mandir}/man1/mint.*
%doc %{_mandir}/man1/oldmono.*
%config %{_sysconfdir}/mono/*
%{_bindir}/mbas
%{_bindir}/mcs
%{_bindir}/mint
%{_bindir}/mono
%{_libdir}/*.so.*
%{_libdir}/mono/

%files devel
%defattr(-, root, root)
%doc docs/
%doc %{_mandir}/man5/*
%doc %{_mandir}/man1/cert2spc.*
%doc %{_mandir}/man1/certmgr.*
%doc %{_mandir}/man1/chktrust.*
%doc %{_mandir}/man1/cilc.*
%doc %{_mandir}/man1/disco.*
%doc %{_mandir}/man1/gacutil.*
%doc %{_mandir}/man1/genxs.*
%doc %{_mandir}/man1/ilasm.*
%doc %{_mandir}/man1/makecert.*
%doc %{_mandir}/man1/mcs.*
%doc %{_mandir}/man1/mkbundle.*
%doc %{_mandir}/man1/monoburg.*
%doc %{_mandir}/man1/monodis.*
%doc %{_mandir}/man1/monop.*
%doc %{_mandir}/man1/monostyle.*
%doc %{_mandir}/man1/secutil.*
%doc %{_mandir}/man1/setreg.*
%doc %{_mandir}/man1/signcode.*
%doc %{_mandir}/man1/sn.*
%doc %{_mandir}/man1/soapsuds.*
%doc %{_mandir}/man1/sqlsharp.*
%doc %{_mandir}/man1/wsdl.*
%doc %{_mandir}/man1/xsd.*
%{_bindir}/al
%{_bindir}/cert2spc
%{_bindir}/certmgr
%{_bindir}/chktrust
%{_bindir}/cilc
%{_bindir}/disco
%{_bindir}/gacutil
%{_bindir}/genxs
%{_bindir}/gmcs
%{_bindir}/ilasm
%{_bindir}/jay
%{_bindir}/makecert
%{_bindir}/monodis
%{_bindir}/mono-find-provides
%{_bindir}/mono-find-requires
%{_bindir}/monograph
%{_bindir}/monop
%{_bindir}/monoresgen
%{_bindir}/mkbundle
%{_bindir}/pedump
%{_bindir}/resgen
%{_bindir}/secutil
%{_bindir}/setreg
%{_bindir}/signcode
%{_bindir}/sn
%{_bindir}/soapsuds
%{_bindir}/sqlsharp
%{_bindir}/wsdl
%{_bindir}/wsdl2
%{_bindir}/xsd
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mono/
%{_datadir}/mono/
%{_datadir}/jay/
%exclude %{_datadir}/libgc-mono/
%exclude %{_libdir}/*.la

%changelog
* Wed Dec 15 2004 Justin Ross <jross@dhcp83-29.boston.redhat.com> 
- Initial build.
