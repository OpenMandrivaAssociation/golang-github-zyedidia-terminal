# Run tests in check section
%bcond_without check

%global goipath         github.com/zyedidia/terminal
%global commit          1760577dbc0058809dd115a6bfe5999b6b24ab53

%global common_description %{expand:
Vt10x terminal emulation backend.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.5%{?dist}
Summary: Vt10x terminal emulation backend
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%if %{with check}
BuildRequires: golang(github.com/zyedidia/pty)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q

sed -i 's|"github.com/james4k/termbox-go-noinput"|"github.com/nsf/termbox-go"|;
        s|"j4k.co/terminal"|"github.com/zyedidia/terminal"|' boxterm/main.go


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git1760577
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git1760577
- Replace original "j4k.co/terminal" with the fork

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git1760577
- Replace forked dependency with original one

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180314git1760577
- Update with the new Go packaging

* Fri Jan 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180125git1760577
- Initial package for Fedora

