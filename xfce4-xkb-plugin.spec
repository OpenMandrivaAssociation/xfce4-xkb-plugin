%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A plugin for the Xfce4 panel displaying keyboard layout
Name:		xfce4-xkb-plugin
Version:	0.5.5
Release:	1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-xkb-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(xfce4-panel-1.0) >= 4.4.2
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxklavier) >= 5.0
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-xkb-plugin

%description
A plugin for the Xfce4 panel displaying keyboard layout.
The plugin may be used as an indicator for the current layout
and to switch layouts.
The layouts must be defined either in XF86Config or by 
xetskbmap tool.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/*.a

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%dir %{_datadir}/xfce4/xkb
%{_datadir}/xfce4/xkb/*
%{_datadir}/xfce4/panel-plugins/xkb-plugin.desktop
%{_libdir}/xfce4/panel-plugins/


%changelog
* Sun Feb 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4.3-1mdv2012.0
+ Revision: 777403
- update to new version 0.5.4.3

* Tue Jun 14 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4.1-1
+ Revision: 685174
- update to new version 0.5.4.1

* Mon May 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4.0-2
+ Revision: 681982
- rebuild

* Sun May 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4.0-1
+ Revision: 672528
- update to new version 0.5.4.0

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added missing BR

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Thu Feb 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3.3-4mdv2010.1
+ Revision: 511215
- Patch1: fix some crashes

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 0.5.3.3-3mdv2010.1
+ Revision: 489685
- update patch for new libxklavier

* Wed Jul 08 2009 Götz Waschk <waschk@mandriva.org> 0.5.3.3-2mdv2010.0
+ Revision: 393442
- fix build with new libxklavier (bug #52029)

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3.3-1mdv2009.1
+ Revision: 350223
- update to new version 0.5.3.3

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3.2-2mdv2009.1
+ Revision: 349542
- rebuild for xfce-4.6.0

* Wed Feb 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3.2-1mdv2009.1
+ Revision: 337427
- update to new version 0.5.3.2

* Mon Feb 02 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3.1-1mdv2009.1
+ Revision: 336306
- update to new version 0.5.3.1

* Thu Jan 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3-1mdv2009.1
+ Revision: 335223
- update to new version 0.5.3

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 302158
- update to new version 0.5.2

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-2mdv2009.1
+ Revision: 295036
- rebuild for new Xfce4.6 beta1

* Thu Sep 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 287980
- update to new version 0.5.1
- add missing buildrequires

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-6mdv2009.0
+ Revision: 262417
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-5mdv2009.0
+ Revision: 257028
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-3mdv2008.1
+ Revision: 110146
- correct buildrequires
- use upstream tarball name as a real name
- do not package COPYING and INSTALL files
- use upstream name

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-2mdv2008.0
+ Revision: 30500
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-1mdv2008.0
+ Revision: 30296
- new version

