Name:           mono
Version:        1.1.10
Release:        3
Summary:        a .NET runtime environment

Group:          Development/Languages
License:        GPL, LGPL, MIT X11
URL:            http://www.mono-project.com/
Source0:        mono-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bison, glib2-devel, pkgconfig, libicu-devel libgdiplus

# JIT only availible on these:
ExclusiveArch: %ix86 x86_64 ppc ia64 s390 armv4l sparc

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary:        The Mono CIL runtime, suitable for running .NET code
Group:          Development/Languages

%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

%package devel
Summary:        Development tools and headers for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release
Requires:       glib2-devel

%description devel
This package includes all Mono library headers and completes the
Mono developer toolchain (with the mono profiler, assembler and
other various tools)

%package nunit
Summary:        NUnit Testing Framework
Group:          Development/Languages
Requires:       mono-core == %version-%release
Requires:       glib2-devel

%description nunit
NUnit is a unit-testing framework for all .Net languages. Initially
ported from JUnit, the current release, version 2.2, is the fourth
major release of this Unit based unit testing tool for Microsoft .NET.
It is written entirely in C# and  has been completely redesigned to
take advantage of many .NET language features, for example
custom attributes and other reflection related capabilities. NUnit
brings xUnit to all .NET languages.

%package locale-extras
Summary:        Extra locale information for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

# The above seems safe

%package jscript
Summary:        JScript .NET support for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description jscript
This package contains the JScript .NET compiler and language runtime.
This allows you to compile and run JScript.NET application and
assemblies.

%package basic
Summary:        Visual Basic .NET support for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description basic
This package contains the Visual Basic .NET compiler and language
runtime. This allows you to compile and run VB.NET application and
assemblies.

%package extras
Summary:        Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description extras
This package provides the libary and application to run services
and daemons with Mono. It also includes stubs for the following
.NET 1.1 and 2.0 assemblies: Microsoft.Vsa,
System.Configuration.Install, System.Management, System.Messaging.

%package winforms
Summary:        Windows Forms implementation for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package web
Summary:        ASP.NET, Remoting, and Web Services for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%package data
Summary:        Database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

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
Requires:       mono-core == %version-%release
Requires:       sqlite

%description data-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package data-sybase
Summary:        Sybase database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description data-sybase
This package contains the ADO.NET Data provider for the Sybase
database.

%package data-oracle
Summary:        Oracle database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%package data-postgresql
Summary:        Postgresql database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description data-postgresql
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%package data-firebird
Summary:        Firebird database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description data-firebird
This package contains the ADO.NET Data provider for the Firebird
database.

# This uses the upstream package name, don't know why its not mono-data-*
%package -n ibm-data-db2
Summary:        IBM DB2 database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description -n ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

# This uses the upstream package name, don't know why its not mono-data-*
%package -n bytefx-data-mysql
Summary:        MySQL database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core == %version-%release

%description -n bytefx-data-mysql
This package contains the ADO.NET Data provider for MySQL. This is
no longer maintained. MySQL AB now provides MySQL Connector/Net
which is fully managed and actively maintained.

%define monodir %_prefix/lib/mono
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

%build
%ifarch ia64 s390
export CFLAGS="-O2 -fno-strict-aliasing"
%else
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%endif

%configure --with-ikvm=yes --with-jit=yes
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# Libtool is on crack, installing the shell wrappers
cp mono/dis/.libs/monodis $RPM_BUILD_ROOT%{_bindir}
cp mono/monograph/.libs/monograph $RPM_BUILD_ROOT%{_bindir}

rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*.la

# We put these inside rpm
rm $RPM_BUILD_ROOT%{_bindir}/mono-find-provides
rm $RPM_BUILD_ROOT%{_bindir}/mono-find-requires

# This was removed upstream:
rm -fr $RPM_BUILD_ROOT%{monodir}/gac/Mono.Security.Win32/[12]*
rm $RPM_BUILD_ROOT%{monodir}/*/Mono.Security.Win32.dll
rm $RPM_BUILD_ROOT%{_datadir}/libgc-mono/README*
rm $RPM_BUILD_ROOT%{_datadir}/libgc-mono/barrett_diagram
rm $RPM_BUILD_ROOT%{_datadir}/libgc-mono/*.html
rm $RPM_BUILD_ROOT%{_datadir}/libgc-mono/gc.man
rm $RPM_BUILD_ROOT%{_mandir}/man1/cilc.1
rm $RPM_BUILD_ROOT/%_bindir/cilc
rm $RPM_BUILD_ROOT%{monodir}/1.0/cilc*
rm $RPM_BUILD_ROOT/%_bindir/jay
rm -r $RPM_BUILD_ROOT%{_datadir}/jay
rm $RPM_BUILD_ROOT%{_prefix}/man/man1/jay.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/monostyle.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/oldmono.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/mint.1
rm $RPM_BUILD_ROOT%{_libdir}/pkgconfig/mint.pc
rm $RPM_BUILD_ROOT%{monodir}/1.0/CorCompare.exe
rm $RPM_BUILD_ROOT%{monodir}/1.0/browsercaps-updater.exe*
rm $RPM_BUILD_ROOT%{monodir}/1.0/mono-api-diff.exe
rm $RPM_BUILD_ROOT%{monodir}/*/mono-api-info.exe
rm -f $RPM_BUILD_ROOT%{_bindir}/monop2
rm -f $RPM_BUILD_ROOT%{monodir}/2.0/monop.exe*
rm -f $RPM_BUILD_ROOT%{_bindir}/nunit-console
rm -f $RPM_BUILD_ROOT%{monodir}/*/nunit-console.exe*
rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoSupportW*
rm -f $RPM_BUILD_ROOT%{monodir}/1.0/mono-shlib-cop.exe.config
rm $RPM_BUILD_ROOT/%_bindir/xbuild

%clean
rm -rf $RPM_BUILD_ROOT

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%{_libdir}/libmono.so*
%{_bindir}/mono
%mono_bin certmgr
%mono_bin chktrust
%mono_bin gacutil
%mono_bin gmcs
%mono_bin mcs
%mono_bin mozroots
%mono_bin setreg
%mono_bin sn
%{_mandir}/man1/certmgr.1.gz
%{_mandir}/man1/chktrust.1.gz
%{_mandir}/man1/gacutil.1.gz
%{_mandir}/man1/mcs.1.gz
%{_mandir}/man1/mono.1.gz
%{_mandir}/man1/mozroots.1.gz
%{_mandir}/man1/setreg.1.gz
%{_mandir}/man1/sn.1.gz
%{_mandir}/man5/mono-config.5.gz
%dir %{monodir}
%dir %{monodir}/1.0
%dir %{monodir}/2.0
%dir %{monodir}/gac
%gac_dll Commons.Xml.Relaxng
%gac_dll I18N
%gac_dll I18N.West
%gac_dll ICSharpCode.SharpZipLib
%gac_dll Microsoft.VisualC
%gac_dll Mono.C5
%gac_dll Mono.Cairo
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.GetOptions
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll System
%gac_dll System.Configuration
%gac_dll System.Drawing
%gac_dll System.Security
%gac_dll System.Xml
%gac_dll cscompmgd
%{monodir}/?.0/mscorlib.dll
%{monodir}/?.0/mscorlib.dll.mdb
%dir /etc/mono
%dir /etc/mono/1.0
%dir /etc/mono/2.0
%config /etc/mono/config
%config /etc/mono/1.0/machine.config
%config /etc/mono/2.0/machine.config
%{_libdir}/libikvm-native.so
%{_libdir}/libMonoPosixHelper.so*

%files devel
%defattr(-,root,root,-)
%{_bindir}/monodis
%{_bindir}/pedump
%{_bindir}/monodiet
%mono_bin al
%mono_bin caspol
%mono_bin cert2spc
%mono_bin dtd2xsd
%mono_bin genxs
%mono_bin ilasm
%mono_bin macpack
%mono_bin makecert
%mono_bin mkbundle
%mono_bin monop
%mono_bin mono-shlib-cop
%mono_bin permview
%mono_bin prj2make
%mono_bin resgen
%mono_bin secutil
%mono_bin signcode
%{monodir}/1.0/ictool.exe
%{monodir}/1.0/ictool.exe.mdb
%{_mandir}/man1/al.1.gz
%{_mandir}/man1/cert2spc.1.gz
%{_mandir}/man1/dtd2xsd.1.gz
%{_mandir}/man1/genxs.1.gz
%{_mandir}/man1/ilasm.1.gz
%{_mandir}/man1/macpack.1.gz
%{_mandir}/man1/makecert.1.gz
%{_mandir}/man1/mkbundle.1.gz
%{_mandir}/man1/mono-shlib-cop.1.gz
%{_mandir}/man1/monodis.1.gz
%{_mandir}/man1/monop.1.gz
%{_mandir}/man1/permview.1.gz
%{_mandir}/man1/prj2make.1.gz
%{_mandir}/man1/secutil.1.gz
%{_mandir}/man1/signcode.1.gz
%gac_dll PEAPI
%{_bindir}/monograph
%{_includedir}/mono
%{_libdir}/libmono-profiler-aot.*
%{_libdir}/libmono-profiler-cov.*
%{_libdir}/pkgconfig/dotnet.pc
%{_libdir}/pkgconfig/mono.pc
%{_mandir}/man1/monoburg.*
%{_datadir}/mono/cil/cil-opcodes.xml
%dir %{_datadir}/mono
%dir %{_datadir}/mono/cil

%files nunit
%defattr(-,root,root,-)
%gac_dll nunit.core
%gac_dll nunit.framework
%gac_dll nunit.util
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

%files basic
%defattr(-,root,root,-)
%mono_bin mbas
%gac_dll Microsoft.VisualBasic

%files extras
%defattr(-,root,root,-)
%{_mandir}/man1/mono-service.1.gz
%mono_bin mono-service
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceProcess
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
%gac_dll System.Runtime.Remoting
%gac_dll System.Web
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.Web.Services
%mono_bin disco
%mono_bin soapsuds
%mono_bin_1 wsdl wsdl
%mono_bin_2 wsdl2 wsdl
%mono_bin xsd
%{_mandir}/man1/disco.1.gz
%{_mandir}/man1/soapsuds.1.gz
%{_mandir}/man1/wsdl.1.gz
%{_mandir}/man1/xsd.1.gz
%config /etc/mono/browscap.ini
%config /etc/mono/1.0/DefaultWsdlHelpGenerator.aspx
%config /etc/mono/2.0/DefaultWsdlHelpGenerator.aspx


%files data
%defattr(-,root,root,-)
%mono_bin sqlsharp
%{_mandir}/man1/sqlsharp.1.gz
%gac_dll System.Data
%gac_dll Mono.Data
%gac_dll Mono.Data.Tds
%gac_dll Mono.Data.TdsClient
%gac_dll System.EnterpriseServices
%gac_dll Novell.Directory.Ldap
%gac_dll System.DirectoryServices

%files data-sqlite
%defattr(-,root,root,-)
%gac_dll Mono.Data.SqliteClient

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

%changelog
* Fri Nov 18 2005 Alexander Larsson <alexl@redhat.com> 1.1.10-3
- New try for s390

* Thu Nov 17 2005 Alexander Larsson <alexl@redhat.com> 1.1.10-2
- Build on s390 and x86-64 now

* Tue Nov 15 2005 Alexander Larsson <alexl@redhat.com> - 1.1.10-1
- Initial version
