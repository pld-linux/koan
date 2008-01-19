Summary:	Network provisioning tool for Xen and Bare Metal Machines
Summary(pl.UTF-8):	Narzędzie do instalacji po sieci maszyn opartych na Xenie i fizycznych
Name:		koan
Version:	0.6.3
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://cobbler.et.redhat.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	3d1ba7f0fa189b986685c817e71ebbd3
URL:		http://cobbler.et.redhat.com/
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%py_requireseq	python
#Requires:	mkinitrd
Requires:	syslinux
# not noarch just because syslinux (gethostip) is not portable
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Koan stands for kickstart-over-a-network and allows for both network
provisioning of new virtualized guests and destructive re-provisioning
of any existing system. For use with a boot-server configured with
'cobbler'.

%description -l pl.UTF-8
Koan to skrót od kickstart-over-a-network (szybkie uruchamianie po
sieci) i pozwala na sieciowe uruchamianie nowych wirtualnych
systemów-gości oraz destrukcyjną podmianę dowolnego istniejącego
systemu. Do używania z serwerem startowym skonfigurowanym przy użyciu
cobblera.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=1 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CHANGELOG README
%attr(755,root,root) %{_bindir}/koan
%dir %{py_sitescriptdir}/koan
%{py_sitescriptdir}/koan/*.py[co]
%dir /var/spool/koan
%{_mandir}/man1/koan.1*
