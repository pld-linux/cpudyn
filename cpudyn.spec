Summary:	A tools to control CPU frequency
Summary(pl):	Narz�dzia do kontroli cz�stotliwo�ci procesora
Name:		cpudyn
Version:	1.0
Release:	0.2
License:	GPL
Group:		Daemons
Source0:	http://mnm.uib.es/~gallir/cpudyn/download/%{name}-%{version}.tgz
# Source0-md5:	2922149f624a07b3d6f012a084e89e7a
Source1:	%{name}.init
Source2:	%{name}.conf
URL:		http://mnm.uib.es/~gallir/cpudyn/
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	cpufreqd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program control the speed in Intel SpeedStep, Pentium 4 Mobile
and PowerPC machines with the cpufreq compiled in the kernel.

Tested with 2.4, Pentium 3 Speedstep Laptop (Dell Latitude), Pentium 4
Mobile Laptop (Dell Inspiron), AMD Power Now, Apple iBook, IBM
Thinkpad. cpudyn is just a user space program, so it will work on
every processor supported by the kernel's cpufreq driver.

%description -l pl
Ten program kontroluje pr�dko�� procesor�w Intel SpeedStep, Pentium 4
Mobile oraz PowerPC (o ile kernel zosta� skompilowany z obs�ug�
cpufreq).

Program ten zosta� przetestowany na j�drze 2.4, na Pentium 3 SpeedStep
(Dell Latitude), Pentium 4 Mobile (Dell Inspiron), AMD Power Now,
Apple iBook, IBM Thinkpad. cpudyn jest programem userspace, wi�c
b�dzie wsp�pracowa� z ka�dym procesorem wspieranym przez sterownik
cpufreq.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sysconfdir},/etc/rc.d/init.d/,%{_mandir}/man8}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/cpudynd
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/cpudyn.conf
install cpudynd $RPM_BUILD_ROOT/sbin
install cpudynd.8 $RPM_BUILD_ROOT%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README faq.html
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cpudyn.conf
%attr(755,root,root) /sbin/cpudynd
%attr(754,root,root) /etc/rc.d/init.d/cpudynd
%{_mandir}/man8/*
