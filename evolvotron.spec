%define name evolvotron
%define version 0.4.0
%define release %mkrel 4

Summary: Interactive "generative art" software
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/evolvotron/%{name}-%{version}.tar.bz2
Patch: evolvotron-0.4.0-gcc4.1.patch
License: GPL
Group: Toys
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://evolvotron.sf.net
Buildrequires: qt3-devel

%description
Evolvotron Interactive "generative art" software to evolve
images/textures/patterns through an iterative process of random
mutation and user-selection driven evolution.  If you like lava lamps,
and still think the Mandelbrot set is cool, this could be the software
for you.

%prep
%setup -q -n %name
%patch -p1

%build
export QTDIR=%_prefix/lib/qt3
export PATH=$QTDIR/bin:$PATH
./configure fs
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
install -m 755 evolvotron/evolvotron evolvotron_mutate/evolvotron_mutate \
  evolvotron_render/evolvotron_render %buildroot%_bindir

install -d $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): \
needs="x11" \
section="More Applications/Games/Toys" \
title="Evolvotron" \
longtitle="Interactive generative art software" \
command="%{name}" \
icon="toys_section.png" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Evolvotron
Comment=Interactive generative art software
Exec=%{name}
Icon=toys_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Toys;Amusement;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
 
%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE TODO
%_bindir/%{name}*
%_datadir/applications/mandriva*
%_menudir/%name


