p=load(["Fetal_Brain_FSE_Images.mat"],"FSE_Images").FSE_Images;
for i=1:50
    figure(1)
    imagesc(real(p(:,:,i)))
    colormap("gray")
    colorbar
    axis image
    pause(1)
end