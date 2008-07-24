%define name evolvotron
%define version 0.5.1
%define release %mkrel 3

Summary: Interactive "generative art" software
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/evolvotron/%{name}-%{version}.tar.gz
License: GPL
Group: Toys
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://evolvotron.sf.net
Buildrequires: qt3-devel
Buildrequires: boost-devel

%description
Evolvotron Interactive "generative art" software to evolve
images/textures/patterns through an iterative process of random
mutation and user-selection driven evolution.  If you like lava lamps,
and still think the Mandelbrot set is cool, this could be the software
for you.

%prep
%setup -q -n %name

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
Categories=Qt;Amusement;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE TODO
%_bindir/%{name}*
%_datadir/applications/mandriva*


