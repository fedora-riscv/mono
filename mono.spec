# Based off of a spec file by Dag Wieers <dag@wieers.com>
# http://dag.wieers.com/packages/mono/mono.spec

Summary: Mono CIL runtime
Name: mono
Version: 1.1.3
Release: 3
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

%package data
Summary: mono-data
Group: Development/Libraries
Requires: %{name}-enterprise = %{version}-%{release}

%description data
mono-data

%package data-db2
Summary: mono-data-db2
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}

%description data-db2
mono-data-db2

%package data-mysql
Summary: mono-data-mysql
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-design = %{version}-%{release}
Requires: %{name}-sharpziplib = %{version}-%{release}
Requires: %{name}-posix = %{version}-%{release}

%description data-mysql
mono-data-mysql

%package data-oracle
Summary: mono-data-oracle
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}

%description data-oracle
mono-data-oracle

%package data-postgresql
Summary: mono-data-postgresql
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-design = %{version}-%{release}

%description data-postgresql
mono-data-postgresql

%package data-sqlite
Summary: mono-data-sqlite
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}

%description data-sqlite
mono-data-sqlite

%package data-sybase
Summary: mono-data-sybase
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}

%description data-sybase
mono-data-sybase

%package data-tds
Summary: mono-data-tds
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}

%description data-tds
mono-data-tds

%package design
Summary: mono-design
Group: Development/Libraries
Requires: %{name}-winforms = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}

%description design
mono-design

%package devel
Summary: mono-devel
# Fix group XXX
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
mono-devel

%package basic
Summary: mono-basic
# Fix group XXX
Group: Development/Libraries
Requires: %{name}-winforms = %{version}-%{release}

%description basic
mono-basic

%package directory
Summary: mono-directory
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description directory
mono-directory

%package drawing
Summary: mono-drawing
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description drawing
mono-drawing

%package enterprise
Summary: mono-enterprise
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description enterprise
mono-enterprise

%package extra-assemblies
Summary: mono-extra-assemblies
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description extra-assemblies
mono-extra-assemblies

%package messaging
Summary: mono-messaging
Group: Development/Libraries
Requires: %{name}-enterprise = %{version}-%{release}
Requires: %{name}-winforms = %{version}-%{release}

%description messaging
mono-messaging

%package nunit
Summary: mono-nunit
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description nunit
mono-nunit

%package posix
Summary: mono-posix
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description posix
mono-posix

%package security
Summary: mono-security
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description security
mono-security

%package sharpziplib
Summary: mono-sharpziplib
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description sharpziplib
mono-sharpziplib

%package web
Summary: mono-web
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-drawing = %{version}-%{release}
Requires: %{name}-enterprise = %{version}-%{release}
Requires: %{name}-sharpziplib = %{version}-%{release}

%description web
mono-web

%package winforms
Summary: mono-winforms
Group: Development/Libraries
Requires: %{name}-drawing = %{version}-%{release}

%description winforms
mono-winforms

%package xml
Summary: mono-xml
Group: Development/Libraries
Requires: %{name}-data = %{version}-%{release}

%description xml
mono-xml

#%post
#echo "You must install libgdiplus separately."

%prep
%setup -q

%build
%configure
make EXTERNAL_MCS=true

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/man/*

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%doc %{_mandir}/man1/mono.*
%doc %{_mandir}/man1/mint.*
%doc %{_mandir}/man1/oldmono.*
%config %{_sysconfdir}/mono/*
%{_bindir}/mint
%{_bindir}/mono
%{_libdir}/*.so.*
%{_libdir}/mono/1.0/mscorlib.dll
%{_libdir}/mono/1.0/mscorlib.dll.mdb
%{_libdir}/mono/1.0/System.dll
%{_libdir}/mono/gac/System/*
%{_libdir}/mono/1.0/System.Xml.dll
%{_libdir}/mono/gac/System.Xml/*
%{_libdir}/mono/1.0/Mono.Security.dll
%{_libdir}/mono/gac/Mono.Security/*
%{_libdir}/mono/1.0/I18N*.dll
%{_libdir}/mono/gac/I18N*/*

%files data
%defattr(-, root, root)
%{_bindir}/sqlsharp
%{_libdir}/mono/1.0/sqlsharp.exe
%{_libdir}/mono/1.0/sqlsharp.exe.mdb
%{_mandir}/man1/sqlsharp.*
%{_libdir}/mono/1.0/System.Data.dll
%{_libdir}/mono/gac/System.Data/*
%{_libdir}/mono/1.0/Mono.Data.dll
%{_libdir}/mono/gac/Mono.Data/*
%{_libdir}/mono/1.0/Mono.Data.Tds.dll
%{_libdir}/mono/gac/Mono.Data.Tds/*

%files data-db2
%defattr(-, root, root)
%{_libdir}/mono/1.0/IBM.Data.DB2.dll
%{_libdir}/mono/gac/IBM.Data.DB2/*

%files data-mysql
%defattr(-, root, root)
%{_libdir}/mono/1.0/ByteFX.Data.dll
%{_libdir}/mono/gac/ByteFX.Data/*

%files data-oracle
%defattr(-, root, root)
%{_libdir}/mono/1.0/System.Data.OracleClient.dll
%{_libdir}/mono/gac/System.Data.OracleClient/*

%files data-postgresql
%defattr(-, root, root)
%{_libdir}/mono/1.0/Npgsql.dll
%{_libdir}/mono/gac/Npgsql/*

%files data-sqlite
%defattr(-, root, root)
%{_libdir}/mono/1.0/Mono.Data.SqliteClient.dll
%{_libdir}/mono/gac/Mono.Data.SqliteClient/*

%files data-sybase
%defattr(-, root, root)
%{_libdir}/mono/1.0/Mono.Data.SybaseClient.dll
%{_libdir}/mono/gac/Mono.Data.SybaseClient/*

%files data-tds
%defattr(-, root, root)
%{_libdir}/mono/1.0/Mono.Data.TdsClient.dll
%{_libdir}/mono/gac/Mono.Data.TdsClient/*

%files design
%defattr(-, root, root)
%{_libdir}/mono/1.0/System.Design.dll
%{_libdir}/mono/gac/System.Design/*
%{_libdir}/mono/1.0/System.Drawing.Design.dll
%{_libdir}/mono/gac/System.Drawing.Design/*

%files devel
%defattr(-, root, root)
%doc docs/
%{_bindir}/al
%{_libdir}/mono/1.0/al.exe
%{_libdir}/mono/1.0/al.exe.mdb
%{_libdir}/mono/1.0/browsercaps-updater.exe
%{_libdir}/mono/1.0/browsercaps-updater.exe.mdb
%{_bindir}/cilc
%{_libdir}/mono/1.0/cilc.exe
%{_libdir}/mono/1.0/cilc.exe.mdb
%{_mandir}/man1/cilc.*
%{_libdir}/mono/1.0/CorCompare.exe
%{_bindir}/gacutil
%{_libdir}/mono/1.0/gacutil.exe
%{_libdir}/mono/1.0/gacutil.exe.mdb
%{_mandir}/man1/gacutil.*
%{_libdir}/mono/1.0/ictool.exe
%{_libdir}/mono/1.0/ictool.exe.mdb
%{_bindir}/ilasm
%{_libdir}/mono/1.0/ilasm.exe
%{_libdir}/mono/1.0/ilasm.exe.mdb
%{_mandir}/man1/ilasm.*
%{_bindir}/mcs
%{_libdir}/mono/1.0/mcs.exe
%{_libdir}/mono/1.0/mcs.exe.mdb
%{_libdir}/mono/1.0/mcs.exe.config
%{_mandir}/man1/mcs.*
%{_bindir}/mkbundle
%{_libdir}/mono/1.0/mkbundle.exe
%{_libdir}/mono/1.0/mkbundle.exe.mdb
%{_mandir}/man1/mkbundle.*
%{_libdir}/mono/1.0/mono-api-diff.exe
%{_libdir}/mono/1.0/mono-api-info.exe
%{_bindir}/mono-find-provides
%{_libdir}/mono/1.0/mono-find-provides.exe
%{_libdir}/mono/1.0/mono-find-provides.exe.mdb
%{_bindir}/mono-find-requires
%{_libdir}/mono/1.0/mono-find-requires.exe
%{_libdir}/mono/1.0/mono-find-requires.exe.mdb
%{_bindir}/monop
%{_libdir}/mono/1.0/monop.exe
%{_libdir}/mono/1.0/monop.exe.mdb
%{_mandir}/man1/monop.*
%{_bindir}/resgen
%{_libdir}/mono/1.0/resgen.exe
%{_libdir}/mono/1.0/resgen.exe.mdb
%{_libdir}/mono/1.0/cscompmgd.dll
%{_libdir}/mono/gac/cscompmgd/*
%{_libdir}/mono/1.0/PEAPI.dll
%{_libdir}/mono/gac/PEAPI/*
%{_libdir}/mono/1.0/Mono.CompilerServices.SymbolWriter.dll
%{_libdir}/mono/gac/Mono.CompilerServices.SymbolWriter/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mono/
%{_datadir}/mono/
%{_bindir}/jay
%{_datadir}/jay/
%{_datadir}/libgc-mono/
%{_bindir}/monodis
%{_mandir}/man1/monodis.*
%{_bindir}/monograph
%{_bindir}/pedump
%{_mandir}/man1/monoburg.*
%{_mandir}/man1/monostyle.*
%{_mandir}/man5/mono-config.*
%exclude %{_bindir}/monoresgen
%exclude %{_libdir}/*.la
%exclude %{_bindir}/gmcs

%files basic
%defattr(-, root, root)
%{_bindir}/mbas
%{_libdir}/mono/1.0/mbas.exe
%{_libdir}/mono/1.0/mbas.exe.mdb
%{_libdir}/mono/1.0/Microsoft.VisualBasic.dll
%{_libdir}/mono/gac/Microsoft.VisualBasic/*

%files directory
%defattr(-, root, root)
%{_libdir}/mono/1.0/System.DirectoryServices.dll
%{_libdir}/mono/gac/System.DirectoryServices/*
%{_libdir}/mono/1.0/Novell.Directory.Ldap.dll
%{_libdir}/mono/gac/Novell.Directory.Ldap/*

%files drawing
%defattr(-, root, root)
%{_libdir}/mono/1.0/Mono.Cairo.dll
%{_libdir}/mono/gac/Mono.Cairo/*
%{_libdir}/mono/1.0/System.Drawing.dll
%{_libdir}/mono/gac/System.Drawing/*

%files enterprise
%defattr(-, root, root)
%{_libdir}/mono/1.0/System.EnterpriseServices.dll
%{_libdir}/mono/gac/System.EnterpriseServices/*
%{_libdir}/mono/1.0/System.Configuration.Install.dll
%{_libdir}/mono/gac/System.Configuration.Install/*
%{_libdir}/mono/1.0/System.Management.dll
%{_libdir}/mono/gac/System.Management/*

%files extra-assemblies
%defattr(-, root, root)
%{_libdir}/mono/1.0/Microsoft.VisualC.dll
%{_libdir}/mono/gac/Microsoft.VisualC/*
%{_libdir}/mono/1.0/Microsoft.Vsa.dll
%{_libdir}/mono/gac/Microsoft.Vsa/*
%{_libdir}/mono/1.0/System.ServiceProcess.dll
%{_libdir}/mono/gac/System.ServiceProcess/*
%{_libdir}/mono/1.0/Mono.C5.dll
%{_libdir}/mono/gac/Mono.C5/*
%{_libdir}/mono/1.0/Mono.Security.Win32.dll
%{_libdir}/mono/gac/Mono.Security.Win32/*
%{_libdir}/mono/1.0/Mono.GetOptions.dll
%{_libdir}/mono/gac/Mono.GetOptions/*

%files messaging
%defattr(-, root, root)
%{_libdir}/mono/1.0/System.Messaging.dll
%{_libdir}/mono/gac/System.Messaging/*

%files nunit
%defattr(-, root, root)
%{_libdir}/mono/1.0/nunit.core.dll
%{_libdir}/mono/gac/nunit.core/*
%{_libdir}/mono/1.0/nunit.framework.dll
%{_libdir}/mono/gac/nunit.framework/*
%{_libdir}/mono/1.0/nunit.util.dll
%{_libdir}/mono/gac/nunit.util/*

%files posix
%defattr(-, root, root)
%{_libdir}/mono/1.0/Mono.Posix.dll
%{_libdir}/mono/gac/Mono.Posix/*

%files security
%defattr(-, root, root)
%{_bindir}/cert2spc
%{_libdir}/mono/1.0/cert2spc.exe
%{_libdir}/mono/1.0/cert2spc.exe.mdb
%{_mandir}/man1/cert2spc.*
%{_bindir}/certmgr
%{_libdir}/mono/1.0/certmgr.exe
%{_libdir}/mono/1.0/certmgr.exe.mdb
%{_mandir}/man1/certmgr.*
%{_bindir}/chktrust
%{_libdir}/mono/1.0/chktrust.exe
%{_libdir}/mono/1.0/chktrust.exe.mdb
%{_mandir}/man1/chktrust.*
%{_bindir}/makecert
%{_libdir}/mono/1.0/MakeCert.exe
%{_libdir}/mono/1.0/MakeCert.exe.mdb
%{_mandir}/man1/makecert.*
%{_bindir}/secutil
%{_libdir}/mono/1.0/secutil.exe
%{_libdir}/mono/1.0/secutil.exe.mdb
%{_mandir}/man1/secutil.*
%{_bindir}/setreg
%{_libdir}/mono/1.0/setreg.exe
%{_libdir}/mono/1.0/setreg.exe.mdb
%{_mandir}/man1/setreg.*
%{_bindir}/signcode
%{_libdir}/mono/1.0/signcode.exe
%{_libdir}/mono/1.0/signcode.exe.mdb
%{_mandir}/man1/signcode.*
%{_bindir}/sn
%{_libdir}/mono/1.0/sn.exe
%{_libdir}/mono/1.0/sn.exe.mdb
%{_mandir}/man1/sn.*
%{_libdir}/mono/1.0/System.Security.dll
%{_libdir}/mono/gac/System.Security/*

%files sharpziplib
%defattr(-, root, root)
%{_libdir}/mono/1.0/ICSharpCode.SharpZipLib.dll
%{_libdir}/mono/gac/ICSharpCode.SharpZipLib/*

%files web
%defattr(-, root, root)
%{_bindir}/wsdl
%{_bindir}/wsdl2
%{_libdir}/mono/1.0/wsdl.exe
%{_libdir}/mono/1.0/wsdl.exe.mdb
%{_mandir}/man1/wsdl.*
%{_bindir}/soapsuds
%{_libdir}/mono/1.0/soapsuds.exe
%{_libdir}/mono/1.0/soapsuds.exe.mdb
%{_mandir}/man1/soapsuds.*
%{_bindir}/disco
%{_libdir}/mono/1.0/disco.exe
%{_libdir}/mono/1.0/disco.exe.mdb
%{_mandir}/man1/disco.*
%{_libdir}/mono/1.0/System.Web.dll
%{_libdir}/mono/gac/System.Web/*
%{_libdir}/mono/1.0/System.Web.Services.dll
%{_libdir}/mono/gac/System.Web.Services/*
%{_libdir}/mono/1.0/System.Runtime.Remoting.dll
%{_libdir}/mono/gac/System.Runtime.Remoting/*
%{_libdir}/mono/1.0/System.Runtime.Serialization.Formatters.Soap.dll
%{_libdir}/mono/gac/System.Runtime.Serialization.Formatters.Soap/*
%{_libdir}/mono/1.0/Mono.Http.dll
%{_libdir}/mono/gac/Mono.Http/*

%files winforms
%defattr(-, root, root)
%{_libdir}/mono/1.0/Accessibility.dll
%{_libdir}/mono/gac/Accessibility/*
%{_libdir}/mono/1.0/System.Windows.Forms.dll
%{_libdir}/mono/gac/System.Windows.Forms/*

%files xml
%defattr(-, root, root)
%{_bindir}/xsd
%{_libdir}/mono/1.0/xsd.exe
%{_libdir}/mono/1.0/xsd.exe.mdb
%{_mandir}/man1/xsd.*
%{_bindir}/genxs
%{_libdir}/mono/1.0/genxs.exe
%{_libdir}/mono/1.0/genxs.exe.mdb
%{_mandir}/man1/genxs.*
%{_libdir}/mono/1.0/Commons.Xml.Relaxng.dll
%{_libdir}/mono/gac/Commons.Xml.Relaxng/*

%changelog
* Thu Feb 03 2005 Justin Ross <jross@redhat.com>
  - Introduces a more fine-grained packaging scheme.  This
    unfortunately requires detailed file lists.
  - Removes some unused scriptlet code.

* Thu Jan 20 2005 Justin Ross <jross@redhat.com>
  - Moves some binaries from mono to mono-devel.
  - Adds the EXTERNAL_MCS flag to force bootstrap via monolite download.

* Wed Dec 15 2004 Justin Ross <jross@dhcp83-29.boston.redhat.com>
  - Initial build.
