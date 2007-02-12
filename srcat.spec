Summary:	Utility to extract data from a full set of SR disks
Summary(pl.UTF-8):   Narzędzie do wyciągania danych z pełnego zestawu dysków SR
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

%description -l pl.UTF-8
To narzędzie (w stadium alpha) pozwala na wyciągnięcie danych z dysków
używanych w SR. Nie daje żadnej gwarancji.

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
