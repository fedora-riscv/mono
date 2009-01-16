Name:		mono
Version:        2.2
Release:        1%{?dist}
Summary:        A .NET runtime environment

Group:          Development/Languages
License:        MIT
URL:		http://ftp.novell.com/pub/mono/sources-stable/
Source0:        http://ftp.novell.com/pub/mono/sources-stable/%{name}-%{version}.tar.bz2
Source1:	monodir.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bison 
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig
BuildRequires:  libicu-devel
BuildRequires:  libgdiplus-devel >= 2.2
BuildRequires:  zlib-devel
%ifarch ia64
BuildRequires:  libunwind
BuildRequires:  libunwind-devel
%endif
# Required for mono-libdir.patch
BuildRequires: automake libtool gettext-devel
Obsoletes:     monodoc, monodoc-devel

# Yes, mono actually depends on itself, because
# we deleted the bootstrapping binaries. If you
# need to bootstrap mono, comment out this BuildRequires
# and don't delete the binaries in %%prep.

BuildRequires: mono-core

# JIT only availible on these:
ExclusiveArch: %ix86 x86_64 ia64 armv4l sparc alpha s390 s390x ppc

Patch0: mono-2.2-ppc-threading.patch
Patch1: mono-libdir-126.patch
Patch2: mono-1.2.3-use-monodir.patch
Patch3: mono-2.2-uselibdir.patch
Patch4: mono-2.0-monoservice.patch
Patch5: mono-2.0-metadata-makefile.patch
Patch6: mono-22-libgdiwinform.patch
Patch7: mono-22-libdir.patch

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary:        The Mono CIL runtime, suitable for running .NET code
Group:          Development/Languages
Requires:	libgdiplus

%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

%package devel
Summary:        Development tools for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}
Requires:       pkgconfig
Requires:       glib2-devel

%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

%package nunit
Summary:        NUnit Testing Framework
License:	zlib with acknowledgement
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}
Requires:       glib2-devel

%description nunit
NUnit is a unit-testing framework for all .Net languages. Initially
ported from JUnit, the current release, version 2.2, is the fourth
major release of this Unit based unit testing tool for Microsoft .NET.
It is written entirely in C# and  has been completely redesigned to
take advantage of many .NET language features, for example
custom attributes and other reflection related capabilities. NUnit
brings xUnit to all .NET languages.

%package nunit-devel
Summary: pkgconfig for nunit
Group: Development/Libraries
Requires: mono-core = %{version}-%{release}, pkgconfig
Requires: mono-nunit = %{version}-%{release}

%description nunit-devel
Development files for nunit

%package locale-extras
Summary:        Extra locale information for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

%package jscript
Summary:        JScript .NET support for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description jscript
This package contains the JScript .NET compiler and language runtime.
This allows you to compile and run JScript.NET application and
assemblies.

%package extras
Summary:        Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description extras
This package provides the libary and application to run services
and daemons with Mono. It also includes stubs for the following
.NET 1.1 and 2.0 assemblies: Microsoft.Vsa,
System.Configuration.Install, System.Management, System.Messaging.

%package winforms
Summary:        Windows Forms implementation for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package web
Summary:        ASP.NET, Remoting, and Web Services for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%package data
Summary:        Database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description data
This package provides a Mono assembly to facilitate data access
and manipulation with databases, LDAP compatible directory servers
and/or XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command
line sql application as well as the Microsoft SQL Server and ODBC
data providers.

%package data-sqlite
Summary:        sqlite database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}
Requires:       sqlite

%description data-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package data-sybase
Summary:        Sybase database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description data-sybase
This package contains the ADO.NET Data provider for the Sybase
database.

%package data-oracle
Summary:        Oracle database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%package data-postgresql
Summary:        Postgresql database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description data-postgresql
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%package data-firebird
Summary:        Firebird database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description data-firebird
This package contains the ADO.NET Data provider for the Firebird
database.

%package -n ibm-data-db2
Summary:        IBM DB2 database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description -n ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

%package -n bytefx-data-mysql
Summary:        MySQL database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description -n bytefx-data-mysql
This package contains the ADO.NET Data provider for MySQL. This is
no longer maintained. MySQL AB now provides MySQL Connector/Net
which is fully managed and actively maintained.

%package -n monodoc
Summary:	The mono documentation system
Group:		Documentation
Requires:	mono-core = %{version}-%{release}

%description -n monodoc
monodoc is the documentation package for the mono .NET environment

%package -n monodoc-devel
Summary: .pc file for monodoc
Group: Documentation
Requires: monodoc = %{version}-%{release} pkgconfig
Requires: mono-core = %{version}-%{release}

%description -n monodoc-devel
Development file for monodoc

%define monodir %{_libdir}/mono
%define gac_dll(dll)  %{monodir}/gac/%{1} \
  %{monodir}/?.0/%{1}.dll \
  %{nil}
%define mono_bin(bin) %{_bindir}/%{1} \
  %{monodir}/?.0/%{1}.exe \
  %{monodir}/?.0/%{1}.exe.* \
  %{nil}
%define mono_bin_1(bin, dll) %{_bindir}/%{1} \
  %{monodir}/1.0/%{2}.exe \
  %{monodir}/1.0/%{2}.exe.* \
  %{nil}
%define mono_bin_2(bin, dll) %{_bindir}/%{1} \
  %{monodir}/2.0/%{2}.exe \
  %{monodir}/2.0/%{2}.exe.* \
  %{nil}

%prep
%setup -q

%patch0 -p1 -b .ppc-threading
%patch1 -p1 -b .libdir
%patch2 -p1 -b .usemonodir
%patch3 -p1 -b .uselibdir
%patch4 -p1 -b .monoservice
%patch5 -p1 -b .metadata-makefile
%patch6 -p1 -b .libgdiplus
sed -i -e 's!@libdir@!%{_libdir}!' %{PATCH7}
%patch7 -p1 -b .libdir-22
sed -i -e 's!%{_libdir}!@libdir@!' %{PATCH7}
sed -i -e 's!$(prefix)/lib/!%{_libdir}/!' docs/Makefile.{am,in}

autoreconf -f -i -s

# Add undeclared Arg
sed -i "61a #define ARG_MAX	_POSIX_ARG_MAX" mono/io-layer/wapi_glob.h

# Remove prebuilt binaries
rm -rf mcs/class/lib/monolite/*

%build
%ifarch ia64 s390 s390x
export CFLAGS="-O2 -fno-strict-aliasing"
%else
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%endif

gcc -o monodir %{SOURCE1} -DMONODIR=\"%{_libdir}/mono\"

%configure --with-ikvm=yes --with-jit=yes --with-xen_opt=yes --with-moonlight=no --disable-static --with-preview=yes --with-libgdiplus=installed
make


%install
%{__rm} -rf %{buildroot}
make DESTDIR=%{buildroot} install
install monodir %{buildroot}%{_bindir}

%{__rm} %{buildroot}%{_libdir}/*.la

# We put these inside rpm
%{__rm} %{buildroot}%{_bindir}/mono-find-provides
%{__rm} %{buildroot}%{_bindir}/mono-find-requires

# This was removed upstream:
%{__rm} -fr %{buildroot}%{monodir}/gac/Mono.Security.Win32/[12]*
%{__rm} -rf %{buildroot}%{monodir}/1.0/Mono.Security.Win32.dll
%{__rm} -rf %{buildroot}%{monodir}/2.0/Mono.Security.Win32.dll
%{__rm} %{buildroot}%{_datadir}/libgc-mono/README*
%{__rm} %{buildroot}%{_datadir}/libgc-mono/barrett_diagram
%{__rm} %{buildroot}%{_datadir}/libgc-mono/*.html
%{__rm} %{buildroot}%{_datadir}/libgc-mono/gc.man
%{__rm} %{buildroot}/%_bindir/jay
%{__rm} -r %{buildroot}%{_datadir}/jay
%{__rm} %{buildroot}%{_mandir}/man1/jay.1
%{__rm} %{buildroot}%{_mandir}/man1/monostyle.1
%{__rm} %{buildroot}%{_mandir}/man1/oldmono.1
%{__rm} %{buildroot}%{_mandir}/man1/mint.1
%{__rm} %{buildroot}%{monodir}/1.0/browsercaps-updater.exe*
%{__rm} %{buildroot}/%_bindir/smcs
%{__rm} %{buildroot}/%_libdir/pkgconfig/smcs.pc

%find_lang mcs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files core -f mcs.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%{_bindir}/mono
%{_bindir}/monodir
%{_bindir}/mono-api-*
%mono_bin csharp
%{_bindir}/gacutil1
%mono_bin mod
%mono_bin mono-cil-strip
%{monodir}/?.0/mono-api-info*
%{_bindir}/mono-test-install
%{_bindir}/gacutil2
%mono_bin certmgr
%mono_bin chktrust
%mono_bin gacutil
%mono_bin gmcs
%mono_bin mcs
%{_bindir}/mcs1
%mono_bin mozroots
%mono_bin mconfig
%mono_bin setreg
%mono_bin sn
%mono_bin installvst
%mono_bin monolinker
%{monodir}/?.0/installutil.*
%{monodir}/3.5/System.Web.Extensions*
%{monodir}/2.0/System.Xml.Linq.dll
%{_bindir}/mkbundle2
%{_libdir}/libmono.so.*
%{_libdir}/libmono-profiler-logging.so.*
%{_libdir}/mono/1.0/CorCompare.exe
%{_libdir}/mono/1.0/mono-api-diff.exe
%{_libdir}/mono/1.0/transform.exe
%{_mandir}/man1/certmgr.1.gz
%{_mandir}/man1/chktrust.1.gz
%{_mandir}/man1/gacutil.1.gz
%{_mandir}/man1/mcs.1.gz
%{_mandir}/man1/mono.1.gz
%{_mandir}/man1/mozroots.1.gz
%{_mandir}/man1/setreg.1.gz
%{_mandir}/man1/sn.1.gz
%{_mandir}/man1/monolinker.1.gz
%{_mandir}/man1/resgen.1.gz
%{_mandir}/man1/mconfig.1.gz
%{_mandir}/man5/mono-config.5.gz
%{_mandir}/man1/csharp.1.gz
%{_mandir}/man1/mono-cil-strip.1.gz
%{_mandir}/man1/monoburg.1.gz
%{_mandir}/man1/vbnc.1.gz
%{_libdir}/libMonoPosixHelper.so
%dir %{monodir}
%dir %{monodir}/1.0
%dir %{monodir}/2.0
%dir %{monodir}/3.5
%dir %{monodir}/gac
%dir %{monodir}/compat-*
%gac_dll Commons.Xml.Relaxng
%gac_dll I18N
%gac_dll I18N.West
%gac_dll ICSharpCode.SharpZipLib
%{monodir}/compat-*/ICSharpCode.SharpZipLib.dll
%gac_dll Microsoft.VisualC
%gac_dll Mono.C5
%gac_dll Mono.Cairo
%{monodir}/gac/Mono.Cecil
%{monodir}/gac/Mono.Cecil.Mdb
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.GetOptions
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll System
%gac_dll System.Configuration
%gac_dll System.Drawing
%gac_dll System.Security
%gac_dll System.Xml
%gac_dll System.Core
%gac_dll Mono.CSharp
%gac_dll Mono.Management
%gac_dll Mono.Simd
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.IdentityModel.Selectors
%gac_dll System.IdentityModel
%gac_dll System.Runtime.Serialization
%gac_dll cscompmgd
%gac_dll CustomMarshalers
%gac_dll OpenSystem.C
%{monodir}/gac/System.Xml.Linq
%{monodir}/?.0/mscorlib.dll
%{monodir}/?.0/mscorlib.dll.mdb
%dir %{_sysconfdir}/mono
%dir %{_sysconfdir}/mono/1.0
%dir %{_sysconfdir}/mono/2.0
%dir %{_sysconfdir}/mono/mconfig
%config (noreplace) %{_sysconfdir}/mono/config
%config (noreplace) %{_sysconfdir}/mono/1.0/machine.config
%config (noreplace) %{_sysconfdir}/mono/2.0/machine.config
%config (noreplace) %{_sysconfdir}/mono/mconfig/config.xml
%config (noreplace) %{_sysconfdir}/mono/2.0/settings.map
%{_libdir}/mono-source-libs/

%files devel
%defattr(-,root,root,-)
%{_bindir}/monodis
%{_bindir}/pedump
%mono_bin_1 al al
%mono_bin_2 al2 al
%{_bindir}/al1
%mono_bin caspol
%mono_bin cert2spc
%mono_bin cilc
%mono_bin dtd2xsd
%mono_bin dtd2rng
%mono_bin_1 genxs1 genxs
%{_bindir}/genxs
%{_bindir}/genxs2
%mono_bin sgen
%mono_bin_1 ilasm ilasm
%{_bindir}/ilasm1
%mono_bin_2 ilasm2 ilasm
%mono_bin macpack
%mono_bin makecert
%mono_bin mkbundle
%{_bindir}/mkbundle1
%mono_bin_1 monop monop
%{_bindir}/monop1
%mono_bin_2 monop2 monop
%mono_bin mono-shlib-cop
%mono_bin mono-xmltool
%mono_bin permview
%mono_bin prj2make
%mono_bin_1 resgen resgen
%{_bindir}/resgen1
%mono_bin_2 resgen2 resgen
%mono_bin secutil
%mono_bin signcode
%mono_bin xbuild
%{monodir}/1.0/ictool.exe
%{monodir}/1.0/ictool.exe.mdb
%{_mandir}/man1/al.1.gz
%{_mandir}/man1/cert2spc.1.gz
%{_mandir}/man1/cilc.1.gz
%{_mandir}/man1/dtd2xsd.1.gz
%{_mandir}/man1/genxs.1.gz
%{_mandir}/man1/ilasm.1.gz
%{_mandir}/man1/macpack.1.gz
%{_mandir}/man1/makecert.1.gz
%{_mandir}/man1/mkbundle.1.gz
%{_mandir}/man1/mono-shlib-cop.1.gz
%{_mandir}/man1/mono-xmltool.1.gz
%{_mandir}/man1/monodis.1.gz
%{_mandir}/man1/monop.1.gz
%{_mandir}/man1/permview.1.gz
%{_mandir}/man1/prj2make.1.gz
%{_mandir}/man1/secutil.1.gz
%{_mandir}/man1/sgen.1.gz
%{_mandir}/man1/signcode.1.gz
%gac_dll PEAPI
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%gac_dll Microsoft.Build.Tasks
%gac_dll Microsoft.Build.Utilities
%{monodir}/2.0/MSBuild
%{monodir}/2.0/Microsoft.Build.xsd
%{monodir}/2.0/Microsoft.*.targets
%{monodir}/2.0/Microsoft.Common.tasks
%{monodir}/2.0/xbuild.rsp
%{_bindir}/monograph
%{_libdir}/libmono-profiler-aot.*
%{_libdir}/libmono-profiler-cov.*
%{_libdir}/libmono.so
%{_libdir}/libMonoSupportW.so
%{_libdir}/libmono-profiler-logging.so
%{_libdir}/libikvm-native.so
%{_libdir}/pkgconfig/dotnet.pc
%{_libdir}/pkgconfig/mono-cairo.pc
%{_libdir}/pkgconfig/mono.pc
%{_libdir}/pkgconfig/cecil.pc
%{_libdir}/pkgconfig/dotnet35.pc
%{_libdir}/pkgconfig/mono-lineeditor.pc
%{_libdir}/pkgconfig/mono-options.pc
%{_libdir}/pkgconfig/wcf.pc
%{_includedir}/mono-1.0
%{_datadir}/mono-1.0/mono/cil/cil-opcodes.xml
%dir %{_datadir}/mono-1.0
%dir %{_datadir}/mono-1.0/mono
%dir %{_datadir}/mono-1.0/mono/cil
%{_libdir}/mono/1.0/culevel*

%files nunit
%defattr(-,root,root,-)
%mono_bin_1 nunit-console nunit-console
%mono_bin_2 nunit-console2 nunit-console
%gac_dll nunit.core
%gac_dll nunit.framework
%gac_dll nunit.util
%gac_dll nunit.mocks

%files nunit-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/mono-nunit.pc

%files locale-extras
%defattr(-,root,root,-)
%gac_dll I18N.MidEast
%gac_dll I18N.Rare
%gac_dll I18N.CJK
%gac_dll I18N.Other

%files jscript
%defattr(-,root,root,-)
%mono_bin mjs
%gac_dll Microsoft.JScript

%files extras
%defattr(-,root,root,-)
%{_mandir}/man1/mono-service.1.gz
%mono_bin_1 mono-service mono-service
%mono_bin_2 mono-service2 mono-service
%{monodir}/gac/mono-service
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceProcess
%gac_dll System.ServiceModel
%gac_dll System.Configuration.Install
%gac_dll Microsoft.Vsa

%files winforms
%defattr(-,root,root,-)
%gac_dll System.Windows.Forms
%gac_dll Accessibility
%gac_dll System.Design
%gac_dll System.Drawing.Design

%files web
%defattr(-,root,root,-)
%gac_dll Mono.Http
%gac_dll Mono.Web
%gac_dll Mono.WebBrowser
%gac_dll System.Runtime.Remoting
%gac_dll System.Web
%gac_dll System.Runtime.Serialization.Formatters.Soap
%{monodir}/compat-2.0/System.Web.Extensions*dll
%gac_dll System.ServiceModel.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.DynamicData
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Extensions
%mono_bin disco
%mono_bin soapsuds
%mono_bin_1 wsdl wsdl
%{_bindir}/wsdl1
%mono_bin_2 wsdl2 wsdl
%mono_bin_2 xsd2 xsd
%mono_bin_1 xsd xsd
%{_mandir}/man1/disco.1.gz
%{_mandir}/man1/soapsuds.1.gz
%{_mandir}/man1/wsdl.1.gz
%{_mandir}/man1/xsd.1.gz
%config (noreplace) %{_sysconfdir}/mono/browscap.ini
%config (noreplace) %{_sysconfdir}/mono/2.0/Browsers/Compat.browser
%config (noreplace) %{_sysconfdir}/mono/1.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %{_sysconfdir}/mono/2.0/web.config
%mono_bin httpcfg
%{_mandir}/man1/httpcfg.1.gz

%files data
%defattr(-,root,root,-)
%mono_bin sqlsharp
%{_mandir}/man1/sqlsharp.1.gz
%gac_dll System.Data
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Linq
%gac_dll Mono.Data
%gac_dll Mono.Data.Tds
%gac_dll Mono.Data.TdsClient
%gac_dll System.EnterpriseServices
%gac_dll Novell.Directory.Ldap
%gac_dll System.DirectoryServices
%gac_dll System.Transactions

%files data-sqlite
%defattr(-,root,root,-)
%gac_dll Mono.Data.SqliteClient
%gac_dll Mono.Data.Sqlite

%files data-sybase
%defattr(-,root,root,-)
%gac_dll Mono.Data.SybaseClient

%files data-oracle
%defattr(-,root,root,-)
%gac_dll System.Data.OracleClient

%files data-postgresql
%defattr(-,root,root,-)
%gac_dll Npgsql

%files data-firebird
%defattr(-,root,root,-)
%gac_dll FirebirdSql.Data.Firebird

%files -n bytefx-data-mysql
%defattr(-,root,root,-)
%gac_dll ByteFX.Data

%files -n ibm-data-db2
%defattr(-,root,root,-)
%gac_dll IBM.Data.DB2

%files -n monodoc
%defattr(-, root, root)
%{_libdir}/mono/gac/monodoc
%{_libdir}/monodoc/*
%{_libdir}/mono/monodoc/monodoc.dll
%mono_bin mdoc
%{_bindir}/mdoc-*
%{_bindir}/mdass*
%{_bindir}/mdval*
%{_bindir}/mod
%{_bindir}/monodoc*
%{_mandir}/man1/md*
%{_mandir}/man1/monodoc*
%{_mandir}/man5/mdoc*

%files -n monodoc-devel
%defattr (-, root, root)
%{_libdir}/pkgconfig/monodoc.pc

%changelog
* Fri Jan 16 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1
- Bump to 2.2 release
- Huge number of changes since 2.01
- Fix now included so winforms no longer has circular dep
- Obsoletes monodoc

* Sun Nov 02 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0.13
- Add in mono-api-diff and mono-api-info

* Fri Oct 24 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0.12
- Update to 2.0.1
- remove selinux patch
- remove s390 disable

* Tue Oct 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-11.2
- fixed no ownership of etc-mono-mconfig directory

* Sat Oct 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-11.1
- fix the last fix...

* Thu Oct 16 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-11
- correct libdir in mono-cairo.pc file (BZ 467294)

* Fri Oct 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-10
- bump to RC4

* Sun Sep 28 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-9
- backported binaryserialisation and datatable patches
- backported stringreplace optimisation
- bump to RC3

* Thu Sep 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-8
- MimeIcon patch added

* Wed Sep 17 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-7
- TableLayoutSettings fix (bz 462005)

* Tue Sep 09 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-6
- Bump to RC1
- Removed XIM patch
- Added additional configure options
- Fixed spec file

* Fri Aug 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-5
- moved libMonoPosixHelper back to the main package

* Fri Aug 22 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-4
- fix for XIM with en_GB.UTF locale plus others

* Mon Aug 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-3
- removed canna-devel requirements
- bump to preview 2
- removed further bits for moonlight

* Sun Aug 17 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-2
- added Canna-devel BR and R Canna for mwf
- removed the build of moonlight parts
- disable-static on configure

* Sat Aug 02 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-1
- bump to 2.0 preview 1
- alter licence to MIT only
- renamed and clean up patch files
- spec file fixes

* Mon Apr 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-2
- pc file fixes

* Tue Apr 15 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-1
- bump to new beta

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9-7
- since we're not bootstrapping with prebuilt binaries, BR: mono-core

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9-6
- Remove prebuilt binaries

* Wed Apr 09 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9-5
- fix licensing

* Mon Apr 07 2008 Xavier Lamien <lxtnow@gmail.com> - 1.9-4
- Added undeclared function bug #xxxx.

* Mon Mar 17 2008 Xavier Lamien	<lxtnow@gmail.com> - 1.9-3
- Added require on mono-nunit-devel

* Thu Mar 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-2
- bump to preview 4

* Mon Feb 04 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-1
- bump to preview 2
- spec file fixes

* Wed Dec 19 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-6.1
- added BR libunwind-devel for ia64 (bz426180)
- fix for LIBDIR problem

* Tue Dec 16 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-4
- bump new version
- removed more redundant bits
- url fix

* Thu Nov 22 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-1
- bump to preview 2
- removed redundant bits of the spec file

* Thu Nov 15 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.5.2-2
- Added R libgdiplus to the winforms package. Fixes BZ 380131

* Sun Nov 11 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.5.2-1
- Bump to next version

* Fri Nov  9 2007 Ray Strode <rstrode@redhat.com> - 1.2.5.1-4
- Apply dropped patch (bug 371781), found by Eskil Bylund

* Wed Nov  7 2007 Alexander Larsson <alexl@redhat.com> - 1.2.5.1-3
- Fix overflow in Mono.Math.BigInteger class (#367551)
  CVE-2007-5197

* Fri Oct 05 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.2.5.1-1
- bump
- added new parts (mono-linker, resgen and mono-cecil)

* Thu Apr 21 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.2.4-1
- update from 1.2.3

* Sun Apr  1 2007 Matthias Clasen <mclasen@redhat.com> - 1.2.3-3
- Fix a spec format error (#210633)

* Thu Mar 29 2007 Alexander Larsson <alexl@redhat.com> - 1.2.3-2
- Also build on alpha (#232268)

* Thu Feb  8 2007 Alexander Larsson <alexl@redhat.com> - 1.2.3-1
- update to 1.2.3

* Mon Dec  4 2006 Alexander Larsson <alexl@redhat.com> - 1.2.2-1
- update to 1.2.2
- Mark config files as noreplace
- Require pkgconfig in mono-devel
- Run ldconfig in post/postun

* Thu Oct 12 2006 Alexander Larsson <alexl@redhat.com> - 1.1.17.1-3
- Don't use slow TLS approach under xen (#210001) 

* Fri Oct  6 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.17.1-2
- CVE-2006-5072

* Mon Sep  4 2006 Alexander Larsson <alexl@redhat.com> - 1.1.17.1-1
- update to 1.1.17.1
- Add one file nunit-devel package due to packaging guidelines (#205056)

* Fri Aug 18 2006 Alexander Larsson <alexl@redhat.com> - 1.1.16.1-2
- Move gac to libdir to be multilib compat
- rename mono-devtools back to mono-devel
- kill mono-lib and mono-lib-devel

* Mon Aug 10 2006 Alexander Larsson <alexl@redhat.com> - 1.1.16.1-1
- Update to 1.1.16.1
- Split out mono libs and devel headers to fix lib64 conflicts (#199790)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.16-1.1
- rebuild

* Fri Jul  7 2006 Alexander Larsson <alexl@redhat.com> - 1.1.16-1
- update to 1.1.16

* Wed Jun  7 2006 Alexander Larsson <alexl@redhat.com> - 1.1.15-1
- Disabled s390 & s390x for now due to build failure
- Update to 1.1.15

* Wed Apr 26 2006 Alexander Larsson <alexl@redhat.com> - 1.1.13.7-2
- Update to 1.1.13.7

* Fri Mar 10 2006 Bill Nottingham <notting@redhat.com> - 1.1.13.4-2
- rebuild for ppc TLS issue (#184446)

* Fri Mar  3 2006 Christopher Aillon <caillon@redhat.com> - 1.1.13.4-1
- Update to 1.1.13.4
- Add patch so mono doesn't segfault on PPC SMP machines
- Minor spec cleanup

* Thu Mar  2 2006 Ray Strode <rstrode@redhat.com> - 1.1.13.2-5
- Updated patch from Jakub (1.1.13.2-3 to 1.1.13.2-5 are 
  for bug 182965)

* Tue Feb 28 2006 Ray Strode <rstrode@redhat.com> - 1.1.13.2-4
- Updated patch from Paolo Molaro <lupus@ximian.com>

* Mon Feb 27 2006 Ray Strode <rstrode@redhat.com> - 1.1.13.2-3
- Patch from Jakub to make work with SELinux better

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> - 1.1.13.2-2
- Rebuild

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.13.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> - 1.1.13.2-1
- Update to 1.1.13.2

* Fri Jan 13 2006 Alexander Larsson <alexl@redhat.com> - 1.1.13-1
- Update to 1.13
- Add libgdiplus dep to mono-core
- Add s390x to build

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> - 1.1.12.1-1
- Update to 1.1.12.1

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> - 1.1.10-4
- rebuild

* Fri Nov 18 2005 Alexander Larsson <alexl@redhat.com> 1.1.10-3
- Disable s390 due to some build failure

* Thu Nov 17 2005 Alexander Larsson <alexl@redhat.com> 1.1.10-2
- Build on s390 and x86-64 now

* Tue Nov 15 2005 Alexander Larsson <alexl@redhat.com> - 1.1.10-1
- Initial version
