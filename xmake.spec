Summary:	A make designed for constructing multiple complex dependencies
Summary(pl):	make przeznaczony do konstruowania wielu z�o�onych zale�nosci
Name:		xmake
Version:	1.06
Release:	1
License:	Public Domain
Group:		Development/Tools
Source0:	http://apollo.backplane.com/xmake/%{name}-%{version}.tgz
# Source0-md5:	257a2d11061363fd3b26fe3a073f890e
URL:		http://apollo.backplane.com/xmake/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMAKE is similar to other makes in many ways. However, XMAKE is
specifically designed to allow the develop to easily construct
multiple complex dependencies, without worrying about default
rulesets.

%description -l pl
XMAKE jest podobny do innych make w wielu dziedzinach. Mimo to jest
specjalnie przeznaczony do umo�liwienia konstruowania z�o�onych
zale�no�ci bez przejmowania si� domy�lnymi ustawianiami.

%prep
%setup -q -n %{name}

%build
%{__make}
./xmake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install obj/xmake $RPM_BUILD_ROOT%{_bindir}
install xmake.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RELEASE_NOTES
%attr(755,root,root) %{_bindir}/xmake
%{_mandir}/*/*
