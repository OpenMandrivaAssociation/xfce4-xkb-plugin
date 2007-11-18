Summary:	A plugin for the Xfce4 panel displaying keyboard layout
Name:		xfce-xkb-plugin
Version:	0.4.3
Release:	%mkrel 2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-xkb-plugin/xfce4-xkb-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-xkb
Provides:	xfce-xkb
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin for the Xfce4 panel displaying keyboard layout.
The plugin may be used as an indicator for the current layout
and to switch layouts.
The layouts must be defined either in XF86Config or by 
xetskbmap tool.
 
%prep
%setup -qn xfce4-xkb-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

# remove unneeded devel files
rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/*.a

%find_lang xfce4-xkb-plugin

%clean
rm -rf  %{buildroot}

%files -f xfce4-xkb-plugin.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%dir %{_datadir}/xfce4/xkb
%{_datadir}/xfce4/xkb/*
%{_datadir}/*/*/xkb-plugin.desktop
%{_libdir}/xfce4/panel-plugins/
