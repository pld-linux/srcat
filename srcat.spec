Summary:	Utility to extract data from a full set of SR disks
Summary(pl):	Narz�dzie do wyci�gania danych z pe�nego zestawu dysk�w SR
Name:		srcat
Version:	0
Release:	0.alpha.1
License:	BSD
Group:		Applications/File
Source0:	http://dl.sourceforge.net/aoetools/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	999f8f9609dd30245ed50b69f7773070
URL:		http://aoetools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This alpha utility enables the user to extract data from disks that
were used in an SR. No warranty.

%description -l pl
To narz�dzie (w stadium alpha) pozwala na wyci�gni�cie danych z dysk�w
u�ywanych w SR. Nie daje �adnej gwarancji.

%prep
%setup -q -n %{name}-alpha-%{version}

%build
%{__cc} %{rpmcflags} -Wall -o srcat unraid.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install srcat $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README TODO
%attr(755,root,root) %{_bindir}/srcat
