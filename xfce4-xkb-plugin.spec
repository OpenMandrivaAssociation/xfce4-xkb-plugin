%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1

Summary:	A plugin for the Xfce4 panel displaying keyboard layout
Name:		xfce4-xkb-plugin
Version:	0.8.5
Release:	1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-xkb-plugin/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	intltool
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
Requires:	xfce4-panel
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
%configure
%make_build

%install
%make_install

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/*.a

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README*
%dir %{_datadir}/xfce4/xkb
%{_datadir}/xfce4/xkb/*
%{_datadir}/xfce4/panel/plugins/xkb.desktop
%{_libdir}/xfce4/panel/plugins/libxkb.so
%{_datadir}/icons/hicolor/*x*/apps/org.xfce.panel.xkb.png
%{_datadir}/icons/hicolor/scalable/apps/org.xfce.panel.xkb.svg
