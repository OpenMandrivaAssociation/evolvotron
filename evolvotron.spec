%define name evolvotron
%define version 0.6.1
%define release 3

Summary: Interactive "generative art" software
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/evolvotron/%{name}-%{version}.tar.gz
Patch: evolvotron-qmake-name.patch
License: GPLv2+
Group: Toys
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: https://evolvotron.sf.net
Buildrequires: qt4-devel
Buildrequires: boost-devel

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
./BUILD

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
install -m 755 evolvotron/evolvotron evolvotron_mutate/evolvotron_mutate \
  evolvotron_render/evolvotron_render %buildroot%_bindir

mkdir -p %buildroot%_mandir/man1
install -m 644 man/man1/*.1 %buildroot%_mandir/man1

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
%doc USAGE %name.html 
%_bindir/%{name}*
%_mandir/man1/%{name}*.1*
%_datadir/applications/mandriva*




%changelog
* Sat Aug 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.1-2mdv2012.0
+ Revision: 693428
- rebuild

* Tue Aug 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 408725
- update to new version 0.6.1

* Sun Jun 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.0-1mdv2010.0
+ Revision: 390194
- fix build
- new version
- build with qt4
- update file list

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-3mdv2009.0
+ Revision: 244996
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Nov 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.1-1mdv2008.1
+ Revision: 113666
- new version

* Sun Oct 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.0-1mdv2008.1
+ Revision: 100902
- fix buildrequires
- new version
- drop patch
- update menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Wed Jan 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-4mdv2007.0
+ Revision: 112810
- Import evolvotron

* Wed Jan 24 2007 Götz Waschk <waschk@mandriva.org> 0.4.0-4mdv2007.1
- unpack patch

* Thu Aug 03 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-3mdv2007.0
- xdg menu

* Thu Jun 08 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-2mdv2007.0
- fix build
- mkrel

* Mon Jun 27 2005 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdk
- New release 0.4.0

* Fri Aug 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.1-2mdk
- rebuild for new menu

* Fri Jul 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.1-1mdk
- drop merged patch
- New release 0.3.1

* Thu Jul 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- fix build
- update patch
- New release 0.3.0

* Wed Jun 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.2-2mdk
- add source URL
- fix qt path
- patch for new g++ (Christiaan Welvaart)

