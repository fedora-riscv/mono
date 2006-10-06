Name:           mono
Version:        1.1.17.1
Release:        2%{?dist}
Summary:        a .NET runtime environment

Group:          Development/Languages
License:        GPL, LGPL, MIT X11
URL:            http://www.mono-project.com/
Source0:        %{name}-%{version}.tar.gz
Source1:	monodir.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bison
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig
BuildRequires:  libicu-devel
BuildRequires:  libgdiplus-devel
BuildRequires:  zlib-devel
%ifarch ia64
BuildRequires:  libunwind
%endif
# Required for mono-libdir.patch
BuildRequires: automake libtool

# JIT only availible on these:
ExclusiveArch: %ix86 x86_64 ppc ia64 armv4l sparc
# Disabled due to strange build failure:
# s390 s390x

Patch1: mono-1.1.13.4-selinux-ia64.patch
Patch2: mono-1.1.13.4-ppc-threading.patch
Patch3: mono-libdir.patch
Patch4: mono-1.1.17.1-use-monodir.patch
Patch5: mono-CVE-2006-5072-TempFileCollection.patch

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary:        The Mono CIL runtime, suitable for running .NET code
Group:          Development/Languages
Requires:	libgdiplus

# Temporary provides due to transient package, remove when rawhide is settled
Obsoletes:      mono-lib
Provides:       mono-lib

%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

# Mono-basic was removed in 1.1.17
Obsoletes:      mono-basic
Provides:       mono-basic

%package devel
Summary:        Development tools for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}
Requires:       glib2-devel

# Temporary provides due to transient package, remove when rawhide is settled
Obsoletes:      mono-lib-devel
Provides:       mono-lib-devel

%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

# Temporary provides due to transient package, remove when rawhide is settled
Obsoletes:      mono-devtools
Provides:       mono-devtools

%package nunit
Summary:        NUnit Testing Framework
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
Requires: mono-core = %{version}-%{release} pkgconfig

%description nunit-devel
Development files for nunit

%package locale-extras
Summary:        Extra locale information for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

# The above seems safe

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

# This uses the upstream package name, don't know why its not mono-data-*
%package -n ibm-data-db2
Summary:        IBM DB2 database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description -n ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

# This uses the upstream package name, don't know why its not mono-data-*
%package -n bytefx-data-mysql
Summary:        MySQL database connectivity for Mono
Group:          Development/Languages
Requires:       mono-core = %{version}-%{release}

%description -n bytefx-data-mysql
This package contains the ADO.NET Data provider for MySQL. This is
no longer maintained. MySQL AB now provides MySQL Connector/Net
which is fully managed and actively maintained.

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
%patch1 -p1 -b .selinux-ia64
%patch2 -p1 -b .ppc-threading
%patch3 -p1 -b .libdir
%patch4 -p1 -b .use-monodir
%patch5 -p1 -b .CVE-2006-5072

%build
%ifarch ia64 s390
export CFLAGS="-O2 -fno-strict-aliasing"
%else
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%endif
autoreconf --force --install

gcc -o monodir %{SOURCE1} -DMONODIR=\"%{_libdir}/mono\"

%configure --with-ikvm=yes --with-jit=yes
make


%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install monodir $RPM_BUILD_ROOT%{_bindir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.a
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# We put these inside rpm
%{__rm} $RPM_BUILD_ROOT%{_bindir}/mono-find-provides
%{__rm} $RPM_BUILD_ROOT%{_bindir}/mono-find-requires

%{__rm} $RPM_BUILD_ROOT%{_bindir}/mbas

# This was removed upstream:
%{__rm} -fr $RPM_BUILD_ROOT%{monodir}/gac/Mono.Security.Win32/[12]*
%{__rm} $RPM_BUILD_ROOT%{monodir}/*/Mono.Security.Win32.dll
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/README*
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/barrett_diagram
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/*.html
%{__rm} $RPM_BUILD_ROOT%{_datadir}/libgc-mono/gc.man
%{__rm} $RPM_BUILD_ROOT/%_bindir/jay
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/jay
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/jay.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/monostyle.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/oldmono.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/mint.1
%{__rm} $RPM_BUILD_ROOT%{monodir}/1.0/CorCompare.exe
%{__rm} $RPM_BUILD_ROOT%{monodir}/1.0/browsercaps-updater.exe*
%{__rm} $RPM_BUILD_ROOT%{monodir}/1.0/mono-api-diff.exe
%{__rm} $RPM_BUILD_ROOT%{monodir}/*/mono-api-info.exe

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%{_bindir}/mono
%{_bindir}/monodir
%mono_bin certmgr
%mono_bin chktrust
%mono_bin gacutil
%mono_bin gmcs
%mono_bin mcs
%mono_bin mozroots
%mono_bin setreg
%mono_bin sn
%{_libdir}/libmono.so.*
%{_libdir}/libMonoPosixHelper.so
%{_libdir}/libMonoSupportW.so
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
%dir %{monodir}/compat-*
%gac_dll Commons.Xml.Relaxng
%gac_dll I18N
%gac_dll I18N.West
%gac_dll ICSharpCode.SharpZipLib
%{monodir}/compat-*/ICSharpCode.SharpZipLib.dll
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
%gac_dll CustomMarshalers
%{monodir}/?.0/mscorlib.dll
%{monodir}/?.0/mscorlib.dll.mdb
%dir /etc/mono
%dir /etc/mono/1.0
%dir /etc/mono/2.0
%config /etc/mono/config
%config /etc/mono/1.0/machine.config
%config /etc/mono/2.0/machine.config
%{_libdir}/libikvm-native.so

%files devel
%defattr(-,root,root,-)
%{_bindir}/monodis
%{_bindir}/pedump
%{_bindir}/monodiet
%mono_bin al
%mono_bin caspol
%mono_bin cert2spc
%mono_bin cilc
%mono_bin dtd2xsd
%mono_bin dtd2rng
%mono_bin genxs
%mono_bin_1 ilasm ilasm
%mono_bin_2 ilasm2 ilasm
%mono_bin macpack
%mono_bin makecert
%mono_bin mkbundle
%mono_bin_1 monop monop
%mono_bin_2 monop2 monop
%mono_bin mono-shlib-cop
%mono_bin mono-xmltool
%mono_bin permview
%mono_bin prj2make
%mono_bin_1 resgen resgen
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
%{_mandir}/man1/signcode.1.gz
%{_mandir}/man1/monoburg.*
%gac_dll PEAPI
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%gac_dll Microsoft.Build.Tasks
%gac_dll Microsoft.Build.Utilities
%{_bindir}/monograph
%{_libdir}/libmono-profiler-aot.*
%{_libdir}/libmono-profiler-cov.*
%{_libdir}/libmono.so
%{_libdir}/pkgconfig/dotnet.pc
%{_libdir}/pkgconfig/mono-cairo.pc
%{_libdir}/pkgconfig/mono.pc
%{_includedir}/mono
%{_datadir}/mono/cil/cil-opcodes.xml
%dir %{_datadir}/mono
%dir %{_datadir}/mono/cil
%{monodir}/xbuild

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
%config /etc/mono/2.0/web.config

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
%gac_dll System.Transactions

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
