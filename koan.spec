Summary:	Network provisioning tool for Xen and Bare Metal Machines
Name:		koan
Version:	0.6.3
Release:	0.1
Source0:	http://cobbler.et.redhat.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	3d1ba7f0fa189b986685c817e71ebbd3
License:	GPL
Group:		Applications/System
URL:		http://cobbler.et.redhat.com/
BuildRequires:	python-devel
#Requires:	mkinitrd
Requires:	python >= 2.2
Requires:	syslinux
BuildArch:	noarch
# Excluding PPC since syslinux (gethostip) isn't available for ppc
ExcludeArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Koan stands for kickstart-over-a-network and allows for both network
provisioning of new virtualized guests and destructive re-provisioning
of any existing system. For use with a boot-server configured with
'cobbler'

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
%dir /var/spool/koan
%attr(755,root,root) %{_bindir}/koan
%dir %{py_sitescriptdir}/koan
%{py_sitescriptdir}/koan/*.py[co]
%{_mandir}/man1/koan.1*
